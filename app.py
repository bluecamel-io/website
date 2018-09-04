#!/usr/bin/env python3
import os
from flask import Flask
from flask import render_template

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

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT'))
