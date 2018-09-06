from wtforms import Form, StringField, TextAreaField
from wtforms import validators

class ContactForm(Form):
    first_name = StringField(
        'First Name',
        [validators.Required()])
    last_name = StringField(
        'Last Name',
        [validators.Required()])
    email = StringField(
        'Email Address',
        [validators.Required(), validators.Email()])
    subject = StringField(
        'Subject',
        [validators.Required()])
    message = TextAreaField(
        'Message',
        [validators.Required()])
