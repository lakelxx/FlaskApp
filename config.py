#
"""
    config.py
    ~~~~~~~~~~~

    Configuration of the Flask app

    :copyright: lakelxx
    :license:
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """ Configuration """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'liuxxchenzq'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
