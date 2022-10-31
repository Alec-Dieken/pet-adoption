from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPet(FlaskForm):
    '''Form for adding new pet'''

    name = StringField("Pet Name", validators=[InputRequired('Must provide a name')])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('por', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[URL('Must provide a valid URL'), Optional()])
    age = IntegerField("Age", validators=[NumberRange(0, 30, 'Value must be between 0-30')])
    notes = StringField("Notes", validators=[Optional()])


class EditPet(FlaskForm):

    photo_url = StringField("Photo URL", validators=[URL('Must provide a valid URL'), Optional()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField('Available?')