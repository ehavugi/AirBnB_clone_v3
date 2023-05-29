#!/usr/bin/python3

from models import *
from models import storage
from models import classes

from flask import Flask, render_template, Blueprint
from api.v1.views import app_views
import os

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def closeApp(exception=None):
    """ Teardown by closing storage
    """
    storage.close()


if __name__ == "__main__":
    hostname = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = os.environ.get("HBNB_API_PORT", 5000)
    app.run(host=hostname, port=port, threaded=True, debug=False)
