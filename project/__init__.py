# project/__init__.py

import os
from flask import Flask, jsonify


from flask_cors import CORS
# instantiate the db


def create_app():

    # instantiate the app
    app = Flask(__name__)
    CORS(app)
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

  
    # register blueprints
    from project.api.views import base_blueprint
    from project.api.views import swagger_blueprint
    from project.api.views import events_blueprint
    from project.api.views import tickets_blueprint
    from project.api.views import ot_objects_blueprint
    app.register_blueprint(base_blueprint)
    app.register_blueprint(swagger_blueprint)
    app.register_blueprint(events_blueprint)
    app.register_blueprint(tickets_blueprint)
    app.register_blueprint(ot_objects_blueprint)

    return app