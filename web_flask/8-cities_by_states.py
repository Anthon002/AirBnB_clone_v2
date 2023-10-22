#!/usr/bin/python3
"""
This script will display a list of states
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def closedb(exc):
    """ this method will close a database session"""
    storage.close()


@app.route('/cities_by_states')
def states_list():
    """ this will display a HTML tag /states_list route """
    sts = storage.all(State).values()
    return render_template('8-cities_by_states.html', sts=sts)


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
