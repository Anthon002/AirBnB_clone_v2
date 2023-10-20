#!/bin/env/python3
"""
This script displays "Hello HBNB"
	    	     "HBNB"
using flask
"""
from flask import Flask

app = Flask(__name__)

@app.route("/",strict_slashes=False)
def hello_HBNB():
	"""This function displays 'Hello HBNB'"""
	return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
	""" This function displayes 'HBNB'"""
	return "HBNB"


if __name__ == "__main__":
	app.run(host="0.0.0.0")
