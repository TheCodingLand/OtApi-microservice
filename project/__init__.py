# project/__init__.py

import os
from flask import Flask, jsonify, Blueprint

from flask import Flask
from project.api.restplus import api
from project.api.views import ns as ot_events_namespace

from flask_cors import CORS




def create_app():

    app = Flask(__name__)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    # instantiate the app
    api.init_app(blueprint)
    CORS(app)
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    # register namespace
    api.add_namespace(ot_events_namespace)
    app.register_blueprint(blueprint)

    return app