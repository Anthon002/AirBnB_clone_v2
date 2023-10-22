#!/usr/bin/python3
"""This script will start a Flask web application.

listening on 0.0.0.0, port 5000.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ This function will display 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """This method will display 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """This will displays 'C' then  the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):

    """This will display 'Python' then the value of <text>.

    """
    text = text.replace("_", " ")
    return "Python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
def displayNumber(n):
    """ this will display an integer """
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>")
def renderTemplate(n):
    """ renders a template if n is an int """
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

