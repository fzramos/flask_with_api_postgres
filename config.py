import os
basedir = os.path.abspath(os.path.dirname(__file__))
# probably not necessary in this app because we get up the db
# using env_setup.py, not config.py

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or '_random_acts_of_kindness!36'
    # adding or just in case secret_key in .env can't be found

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # silence the depreation warnings