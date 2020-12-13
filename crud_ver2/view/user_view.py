from flask import jsonify, request
from flask.views import MethodView
from pymysql import err
from connection import get_connection
from validation import (
    AccountValidattionError,
    NameValidattionError, 
    BirthdayValidattionError
    )
    

class UserMgmt(MethodView):
    def __init__(self, service):
        self.service = service

    def post(self):
        """
            고객 정보 생성(Presentation Layer)
            Returns :
                201:
                    고객 정보 생성 성공시
                400:
                    잘못된 요청시
            Author :
                taeha7b@gmail.com (김태하)
        """
        try:
            user_info = request.json
            db = get_connection()
            enroll_user = self.service.enroll_user(user_info, db)
            if enroll_user == 'name_validate':
                raise NameValidattionError('올바른 이름이 아닙니다')
            elif enroll_user == 'birthday_validate':
                raise BirthdayValidattionError('생년월일 형식에 맞춰주세요 YYYY-MM-DD')
            elif enroll_user == 'account_validate':
                raise AccountValidattionError('올바른 아이디 형식이 아닙니다.')
            elif enroll_user is False:
                return jsonify({'message': '이미 존재하는 아이디 입니다.'}), 400
            
        except (err.OperationalError, err.InternalError, err.ProgrammingError, err.IntegrityError) as e:
            db.rollback()
            message = {"error_number": e.args[0], "err_value": e.args[1]}
            return jsonify(message), 400

        except NameValidattionError as e:
            return jsonify({'message': e.message}), 400

        except BirthdayValidattionError as e:
            return jsonify({'message': e.message}), 400

        except AccountValidattionError as e:
            return jsonify({'message': e.message}), 400

        else:
            db.commit()
            return jsonify({'message':'SUCCESS'}), 201

        finally:
            db.close()

    def get(self):
        """
            고객 정보 목록 조회(Presentation Layer)
            Returns :
                200:
                    고객 정보 목록 조회 성공시
                400:
                    잘못된 요청시
            Author :
                taeha7b@gmail.com (김태하)
        """
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
        """
            고객 정보 변경(Presentation Layer)
            Returns :
                200:
                    고객 정보 변경 성공시
                400:
                    잘못된 요청시
            Author :
                taeha7b@gmail.com (김태하)
        """
        try:
            user_info = request.json
            db = get_connection()
            update_user = self.service.update_user(user_info, db)
            if update_user == 'name_validate':
                raise NameValidattionError('올바른 이름이 아닙니다')
            elif update_user == 'birthday_validate':
                raise BirthdayValidattionError('생년월일 형식에 맞춰주세요 YYYY-MM-DD')
            elif update_user == 'account_validate':
                raise AccountValidattionError('올바른 아이디 형식이 아닙니다.')
            elif update_user is False:
                return jsonify({'message': '존재 하지 않는 아이디 입니다.'}), 400

        except (err.OperationalError, err.InternalError, err.ProgrammingError, err.IntegrityError) as e:
            db.rollback()
            message = {"error_number": e.args[0], "err_value": e.args[1]}
            return jsonify(message), 400

        except NameValidattionError as e:
            return jsonify({'message': e.message}), 400

        except BirthdayValidattionError as e:
            return jsonify({'message': e.message}), 400

        except AccountValidattionError as e:
            return jsonify({'message': e.message}), 400

        else:
            db.commit()
            return jsonify({'message':'SUCCESS'}), 200

        finally:
            db.close()

    def delete(self):
        """
            고객 정보 삭제(Presentation Layer)
            Returns :
                200:
                    고객 정보 삭제 성공시
                400:
                    잘못된 요청시
            Author :
                taeha7b@gmail.com (김태하)
        """
        try:
            user_info = request.json
            db = get_connection()
            delete_user = self.service.delete_user(user_info, db)
            if delete_user == 'account_validate':
                raise AccountValidattionError('올바른 아이디 형식이 아닙니다.')
            elif delete_user is False:
                return jsonify({'message': '존재 하지 않는 아이디 입니다.'}), 400

        except (err.OperationalError, err.InternalError, err.ProgrammingError, err.IntegrityError) as e:
            db.rollback()
            message = {"error_number": e.args[0], "err_value": e.args[1]}
            return jsonify(message), 400

        except AccountValidattionError as e:
            return jsonify({'message': e.message}), 400

        else:
            db.commit()
            return jsonify({'message':'SUCCESS'}), 200
        finally:
            db.close()


class UserDetail(MethodView):
    def __init__(self, service):
        self.service = service

    def get(self,user_info):
        """
            고객 정보 상세 조회(Presentation Layer)
            Returns :
                200:
                    고객 정보 상세 조회 성공시
                400:
                    잘못된 요청시
            Author :
                taeha7b@gmail.com (김태하)
        """
        try:
            db = get_connection()
            user_detail = self.service.user_detail(user_info, db)
            return jsonify(user_detail), 200

        except:
            return jsonify({'message':'UNSUCCESS'}), 400

        finally:
            db.close()

