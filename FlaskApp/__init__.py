#
"""
    __init__.py
    ~~~~~~~~~~~

    Initialization of the Flask app

    :copyright: lakelxx
    :license:
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from FlaskApp import views, models
