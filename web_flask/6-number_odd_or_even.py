#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Print hello hbnb """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Print hbnb """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ this will display a char C followed by the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ this will print python is cool """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ this will display the number route """
    return '{} is number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ This method will render an HTML page if n is an integer """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ this method will show the number as even or odd """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000)
