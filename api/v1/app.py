#!/usr/bin/python3
"""
Flask module to return text as default route
"""
from flask import Flask, escape, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS
app = Flask(__name__)


app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_app(self):
    '''close session'''
    storage.close()


@app.errorhandler(404)
def padge_not_found(e):
    '''handle unfound pages'''
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    h = '0.0.0.0'
    if getenv('HBNB_API_HOST'):
        h = getenv('HBNB_API_HOST')
    p = '5000'
    if getenv('HBNB_API_PORT'):
        p = getenv('HBNB_API_PORT')
    app.run(debug=True, host=h, port=p, threaded=True)
