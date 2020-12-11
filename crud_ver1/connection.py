import pymysql
from config import database as db

def get_connection():
    connection = pymysql.connect(
        host        = db['host'],
        port        = db['port'],
        user        = db['user'],
        password    = db['password'],
        db          = db['database'],
        cursorclass = pymysql.cursors.DictCursor,
        autocommit  = False
    )

    return connection