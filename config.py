import os
from dotenv import load_dotenv 

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Database configuration
    HOST = os.getenv("HOST")
    DATABASE = os.getenv("DATABASE")
    USERNAME = os.getenv("DB_USERNAME")
    PASSWORD = os.getenv("DB_PASSWORD")
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for signing cookies
    SECRET_KEY = os.getenv("SECRET_KEY")