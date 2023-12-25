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

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a list of states from DBStorage in HTML."""
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda x: x.name)

    return render_template('7-states_list.html', sorted_states=sorted_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
