#!/usr/bin/python3
""" Views implementation
"""
from flask import Flask, jsonify
from api.v1.views import app_views

@app_views.route('/status', strict_slashes=False)
def status_page():
    return jsonify({"status":"OK"})
