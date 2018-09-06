#!/usr/bin/env python3
import os
from flask import Flask, request
from flask import render_template
from forms import ContactForm

app = Flask(__name__)

@app.route('/')
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
        return 'form submitted'
    else:
        form = ContactForm()
        return render_template(
            'contact.html',
            title='Contact',
            form=form)
    # placeholder="Please enter your First Name"
    # data-error="First Name is required."
    # required="required"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT'))
