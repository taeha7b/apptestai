import config

from flask import Flask
from flask_cors import CORS
  
from view import create_endpoints
from model import UserDao
from service import UserService


class Services:
    pass

def create_app(test_config = None):

    app = Flask(__name__)

    #SetUp CORS
    CORS(app)

    #SetUp config
    if test_config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.update(test_config)

    #SetUp Persistence Layer
    user_dao = UserDao()

    #SetUp Business Layer
    services = Services
    services.user_service = UserService(user_dao)

    #SetUp Presentation Layer
    create_endpoints(app, services)

    return app