#!/usr/bin/env python3
import os
from flask import Flask, request
from flask import render_template
from forms import ContactForm

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
from sendgrid.helpers.mail import *

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/ecommerce')
def ecommerce():
    return render_template('ecommerce.html', title='E-commerce')


@app.route('/healthcare')
def healthcare():
    return render_template('healthcare.html', title='Healthcare')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    
    if request.method == 'POST':
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        form = ContactForm()

        #email user provideds --- for testing, put your email into the form
        client_email = request.form.get('email')

        #one of our emails to receive clients email --- change to your email if you wanna test it yourself
        one_of_our_emails = "alecross89@gmail.com"
        
        # getting the message and subject of the email
        content_of_email = request.form.get('message')
        email_subject = request.form.get('subject')
        
        # passing client email into Email class
        from_email = Email(client_email)

        # passing message of email to Content class
        content = Content("text/plain", content_of_email)
        
        # passing our email to Email class
        to_email = Email(one_of_our_emails)
    
        mail = Mail(from_email, email_subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return 'form submitted'
    else:
        form = ContactForm()
        return render_template(
            'contact.html',
            title='Contact',
            form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT'))

