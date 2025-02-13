#!/usr/bin/python3
<<<<<<< HEAD
"""starts a flask web application that listens on 0.0.0.0 port 5000"""
=======
"""starts a flask web application
listening on 0.0.0.0 port 5000
"""
>>>>>>> ee7d4282272059bdc4332e07909ded1079c88667

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Return specified string
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return specified string
    """
    return 'HBNB'


@app.route('/c/<text>')
def cText(text):
    """Return reformatted text
    """
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
