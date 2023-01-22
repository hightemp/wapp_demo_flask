import os
import sys

basedir = os.path.abspath(os.path.dirname(sys.argv[0]))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'wapp_demo_flask.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False