
from flask_wtf import Form

from wtforms import TextField, BooleanField, TextAreaField, SubmitField, validators, ValidationError
from wtforms.validators import Required

class ContactForm(Form):
    name = TextField("Name",  [validators.Required()])
    email = TextField("Email",  [validators.Required(), validators.Email()])
    subject = TextField("Subject",  [validators.Required()])
    message = TextAreaField("Message",  [validators.Required()])
    submit = SubmitField("Send")