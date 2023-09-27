#!/usr/bin/python3
<<<<<<< HEAD
"""A script that starts a flask web application that listens on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return a given string"""
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
=======
"""starts a flask web application
listening on 0.0.0.0 port 5000
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_flask():
    """Return specific string
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
>>>>>>> ee7d4282272059bdc4332e07909ded1079c88667
