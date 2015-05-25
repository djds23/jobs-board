from flask.ext.wtf import Form
from flask_security import RegisterForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms_alchemy import model_form_factory

ModelForm = model_form_factory(Form)

class ExtendedRegisterForm(RegisterForm):
    username = StringField('Username', [DataRequired()])
    first_name = StringField('First Name', [DataRequired()])
    last_name = StringField('Last Name', [DataRequired()])
