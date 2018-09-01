from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Dockerized Flask Landing Page'


@app.route('/ecommerce')
def ecommerce():
    return 'Dockerized Flask E-Commerce Page'


@app.route('/healthcare')
def healthcare():
    return 'Dockerized Flask Healthcare Page'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
