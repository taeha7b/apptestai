from flask import Flask
from flask_cors import CORS

from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker

def create_app(test_config = None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.update(test_config)

    # pool size : 10, max_overflow=1 인 QueuePool로 DB 연결 설정
    database = create_engine(app.config['DB_URL'], encoding ='utf-8', pool_size = 10, max_overflow = 1, poolclass = QueuePool)

    # database engin와 연동된 session maker 생성, connection 필요시마다 session instance 생성
    Session = sessionmaker(bind = database)

    # CORS 설정
    CORS(app, resources={r'*': {'origins': '*'}})

    # Persistence layer


    # Business layer


    # Presentation layer


    return app