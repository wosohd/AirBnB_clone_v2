#!/usr/bin/python3
<<<<<<< HEAD
"""script that starts a Flask web application"""
=======
"""starts a flask web application
listening on 0.0.0.0 port 5000
"""

>>>>>>> ee7d4282272059bdc4332e07909ded1079c88667
from flask import Flask, render_template
app = Flask(__name__)


<<<<<<< HEAD
@app.route('/', strict_slashes=False)
def hello():
    """Returns a given string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a given string"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """display C followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text="is cool"):
    """display Python"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """display a HTML page"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n=None):
    """display a HTML page"""
    if isinstance(n, int):
        if n % 2:
            eo = "odd"
        else:
            eo = "even"
        return render_template("6-number_odd_or_even.html", n=n, eo=eo)


if __name__ == "__main__":
    app.run()
=======
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


@app.route('/number_template/<int:n>')
def number_template(n):
    """Displays HTML text is n is a valid interger
    """
    path = '5-number.html'
    return render_template(path, n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Render template based on condition
    """
    path = '6-number_odd_or_even.html'
    return render_template(path, n=n)

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
>>>>>>> ee7d4282272059bdc4332e07909ded1079c88667
