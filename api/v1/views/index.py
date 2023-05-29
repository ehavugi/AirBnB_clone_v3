#!/usr/bin/python3
""" Views implementation
"""
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
from models import classes
from models.state import State

@app_views.route('/status', strict_slashes=False)
def status_page():
    """Returns status page with status set to OK
    """
    return jsonify({"status": "OK"})

@app_views.route("/stats", strict_slashes=False)
def stats():
    """Returns stats for every class implemented
    """
    stats = {key:storage.count(classes[key]) for key in classes}
    return jsonify(stats)
