#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the SQLAlchemy session after each request."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays a list of states with their associated cities in HTML."""
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda x: x.name)

    return render_template('8-cities_by_states.html', sorted_states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
