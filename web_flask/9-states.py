#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the SQLAlchemy session after each request."""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """Displays a list of states in HTML."""
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda x: x.name)

    return render_template('9-states.html', sorted_states=sorted_states)


@app.route('/states/<state_id>', strict_slashes=False)
def state_cities(state_id):
    """Displays cities associated with a state."""
    state = storage.get(State, state_id)
    if state:
        return render_template('9-states_by_id.html', state=state)
    return render_template('9-not_found.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)