from flask import g, Flask, request, send_file, redirect, session, jsonify
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

from .routes.main import main
from .routes.api import api

from .extensions import db, migrate

from config import Config

DATABASE = './wapp_books_manager_flask.db'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main)
    app.register_blueprint(api)

    cache = Cache(app)

    return app
