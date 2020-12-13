import config

from flask import Flask
from flask_cors import CORS
  
from view import create_endpoints
from model import UserDao
from service import UserService

from sqlalchemy          import create_engine
from sqlalchemy.pool     import QueuePool
from sqlalchemy.orm      import sessionmaker
from config import DB_URL

class Services:
    pass

def create_app(test_config = None):

    app = Flask(__name__)

    #SetUp config
    if test_config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.update(test_config)

    # database engin와 연동된 session maker 생성, connection 필요시마다 session instance 생성
    # 

    database = create_engine(DB_URL, encoding ='utf-8', pool_size = 10, max_overflow = 5, poolclass = QueuePool)
  
    Session = sessionmaker(bind = database)
    session = Session()

    #SetUp CORS
    CORS(app)


    #SetUp Persistence Layer
    user_dao = UserDao()

    #SetUp Business Layer
    services = Services
    services.user_service = UserService(user_dao)

    #SetUp Presentation Layer
    create_endpoints(app, services, session)

    return app