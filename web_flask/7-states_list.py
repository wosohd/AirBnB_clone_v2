#!/usr/bin/python3
<<<<<<< HEAD
"""Importing Flask"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """Display States created"""
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """Remove current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
=======
"""starts a flask web application
listening on 0.0.0.0 port 5000
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """Render state_list html page
    """
    path = '7-states_list.html'
    states = storage.all(State)
    # sort State object alphabetically by name
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, sorted_states=sorted_states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """Remove current session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
>>>>>>> ee7d4282272059bdc4332e07909ded1079c88667
    app.run(host='0.0.0.0', port=5000)
