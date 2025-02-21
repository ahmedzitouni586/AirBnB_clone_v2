#!/usr/bin/python3
"""Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list", strict_slashes=False)
def state_list():
    return render_template("7-states_list.html",
                           data=storage.all(State).values())


@app.teardown_appcontext
def storage_close(var=None):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0' port=5000)
