from flask import jsonify, request
from flask.views import MethodView
from pymysql import err
from connection import get_connection

class UserMgmt(MethodView):
    def __init__(self, service):
        self.service = service

    def post(self):
        try:
            user_info = request.json
            db = get_connection()
            enroll_user = self.service.enroll_user(user_info, db)
            
        except (err.OperationalError, err.InternalError, err.ProgrammingError, err.IntegrityError) as e:
            db.rollback()
            message = {"error_number": e.args[0], "err_value": e.args[1]}
            return jsonify(message), 400

        else:
            db.commit()
            return jsonify({'message':'SUCCESS'}), 200
        finally:
            db.close()

    def get(self):
        try:
            db = get_connection()
            page = request.args.get('page')
            user_list = self.service.user_list(page, db)
            return jsonify(user_list), 200

        except:
            return jsonify({'message':'UNSUCCESS'}), 400

        finally:
            db.close()

    def put(self):
        try:
            user_info = request.json
            db = get_connection()
            update_user = self.service.update_user(user_info, db)
            
        except (err.OperationalError, err.InternalError, err.ProgrammingError, err.IntegrityError) as e:
            db.rollback()
            message = {"error_number": e.args[0], "err_value": e.args[1]}
            return jsonify(message), 400

        else:
            db.commit()
            return jsonify({'message':'SUCCESS'}), 200
        finally:
            db.close()

    def delete(self):
        try:
            user_info = request.json
            db = get_connection()
            delete_user = self.service.delete_user(user_info, db)
            
        except (err.OperationalError, err.InternalError, err.ProgrammingError, err.IntegrityError) as e:
            db.rollback()
            message = {"error_number": e.args[0], "err_value": e.args[1]}
            return jsonify(message), 400

        else:
            db.commit()
            return jsonify({'message':'SUCCESS'}), 200
        finally:
            db.close()


class UserDetail(MethodView):
    def __init__(self, service):
        self.service = service

    def get(self,account):
        try:
            db = get_connection()
            user_detail = self.service.user_detail(account, db)
            return jsonify(user_detail), 200

        except:
            return jsonify({'message':'UNSUCCESS'}), 400

        finally:
            db.close()