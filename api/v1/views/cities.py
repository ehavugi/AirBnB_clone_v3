#!/usr/bin/python3
""" Views implementation. For different end points
"""
from flask import Flask, jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models import classes
from models.state import State
from models.city import City


@app_views.route('/cities/<cityid>', strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])
def city_info(cityid):
    """Handles, GET method for getting state info with stateid
                PUT method  for update the state info
                DELETE method for deleting the state info
    """
    if request.method == "GET":
        cities = storage.all(City)
        for city in cities:
            if cities[city].id == cityid:
                return jsonify(cities[city].to_dict())
        abort(404)
    if request.method == "DELETE":
        states = storage.all(City)
        for state in states:
            if states[state].id == cityid:
                storage.delete(states[state])
                storage.save()
                return jsonify({})
        abort(404)
    if request.method == "PUT":
        ignore_keys = ["id", "created_at", "updated_at"]
        data = request.get_json()
        if data is None:
            abort(400, "Not a JSON")
        states = storage.all(City)
        for state in states:
            if states[state].id == cityid:
                for key in data.keys():
                    if not (key in ignore_keys):
                        setattr(states[state], key, data[key])
                states[state].save()
                return jsonify(states[state].to_dict())
        abort(404)


@app_views.route("/cities", strict_slashes=False, methods=['POST', 'GET'])
def city_list():
    """Returns stats for every class implemented
    """
    if request.method == "GET":
        states = storage.all(City)
        if len(states) != 0:
            states = [state.to_dict() for state in states.values()]
        return jsonify(states)
    if request.method == "POST":
        data = request.get_json()
        if data is None:
            abort(400, "Not a JSON")
        if 'name' not in data:
            abort(400, "Missing name")
        new_state = City(**data)
        new_state.save()
        return jsonify(new_state.to_dict()), 201
