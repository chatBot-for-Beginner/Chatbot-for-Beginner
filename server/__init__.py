from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
import config

from api import *
def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        return 'hello'

    return app
