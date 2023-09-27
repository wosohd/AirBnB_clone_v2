#!/usr/bin/python3
<<<<<<< HEAD
"""script that starts a Flask web application"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Returns a given string"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns a given string"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """display C"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """display Python"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def isNumber(n):
    """display 'n is a number” only if n is an integer'"""
    if isinstance(n, int):
        return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)

=======
"""starts a flask web application
listening on 0.0.0.0 port 5000
"""

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


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Displays Python followed by value of text variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """Displays n if path variable is a valid integer
    """
    return str(n) + ' is a number'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
>>>>>>> ee7d4282272059bdc4332e07909ded1079c88667
