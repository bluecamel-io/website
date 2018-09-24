#!/usr/bin/env python3
import os
from flask import Flask, request
from flask import render_template
from forms import ContactForm
from flask import abort

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
from sendgrid.helpers.mail import *

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

# @app.route('/ecommerce')
# def ecommerce():
#     return render_template('ecommerce.html', title='E-commerce')
#
#
# @app.route('/healthcare')
# def healthcare():
#     return render_template('healthcare.html', title='Healthcare')
#
# @app.route('/about')
# def about():
#     return render_template('about.html', title='About')

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':
        form = ContactForm()

        sg = sendgrid.SendGridAPIClient(
            apikey=os.environ.get('SENDGRID_API_KEY'))

        # email user provides
        from_email = Email(
            email=request.form.get('email'),
            name='{first} {last}'.format(
                first=request.form.get('first_name'),
                last=request.form.get('last_name')))

        # format the email subject line
        email_subject = '[Data Science Consulting]: ' + \
            '{subject}'.format(subject=request.form.get('subject'))

        # retrieve the email body
        content = Content("text/plain", request.form.get('message'))

        # create a personalization object to hold all the recipient emails
        to_emails = [
            Email(email='providence.can@gmail.com ', name='Gideon Providence'),
            Email(email='alecross89@gmail.com', name='Alec Ross'),
            Email(email='andrew.ross.mail@gmail.com', name='Andrew Ross')]
        personalization = Personalization()
        for email in to_emails:
            personalization.add_to(email)

        # populate the Mail object
        mail = Mail(
            from_email=from_email,
            subject=email_subject,
            to_email=None,
            content=content)
        mail.add_personalization(personalization)

        response = sg.client.mail.send.post(request_body=mail.get())

        return render_template('form_submitted.html', title='Form_Submitted')
    else:
        form = ContactForm()
        return render_template(
            'contact.html',
            title='Contact',
            form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT'))
