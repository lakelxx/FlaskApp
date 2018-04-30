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


# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# CSRF_ENABLED = True
# SECRET_KEY = 'liuxxchenzq'

# OPENID_PROVIDERS = [
#     { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
#     { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#     { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#     { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#     { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
