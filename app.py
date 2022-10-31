from flask import Flask, render_template, request, redirect, flash
from models import connect_db, db, Pet
from forms import AddPet, EditPet

app = Flask(__name__)
app.config["SECRET_KEY"] = "BlahBlahBlah"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user123:password123@localhost:5432/pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

with app.app_context():
    # db.drop_all()
    db.create_all()
    

@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def addpet():
    form = AddPet()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        if not photo_url:
            photo_url = '/static/images/default.jpg'

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('add_pet_form.html', form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def petview(pet_id):
    pet = Pet.query.get(pet_id)
    form = EditPet()
    

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect(f'/{pet_id}')
    else:
        if pet:
            form.photo_url.default = pet.photo_url
            form.notes.default = pet.notes
            form.available.default = pet.available
            form.process()
            return render_template('petview.html', pet=pet, form=form)
        else:
            return redirect('/')