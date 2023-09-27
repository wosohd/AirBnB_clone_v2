#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Shows the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
"""starts a flask web application
listening on 0.0.0.0 port 5000
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters')
def hbnb_filters():
    """Displays HBnB filters HTML page
    """
    path = '10-hbnb_filters.html'
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template(path, states=states, amenities=amenities)


@app.teardown_appcontext
def app_teardown(arg=None):
    """Remove current session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
>>>>>>> ee7d4282272059bdc4332e07909ded1079c88667
