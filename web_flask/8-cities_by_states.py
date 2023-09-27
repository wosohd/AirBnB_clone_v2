#!/usr/bin/python3
<<<<<<< HEAD
"""Importing Flask"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ Method to close the session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays a html page with states and cities"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
=======
"""Start web application with two routings
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states')
def states_list():
    """Displays a html page with states and cities
    """
    path = '8-cities_by_states.html'
    states = storage.all(State)

    # sort State object alphabetically by name
    # sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, states=states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """Remove current session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
>>>>>>> ee7d4282272059bdc4332e07909ded1079c88667
