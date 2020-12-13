import datetime
from validation import (
    account_validate,
    name_validate, 
    birthday_validate
    )

class UserService:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def enroll_user(self, user_info, session):
        """
            고객 정보 생성(Business Layer)
            Args :
                user_info: 고객 데이터
                db : 데이터베이스 연결객체
            Returns :
                name_validate: 이름에 문제 발생시
                birthday_validate: 생년월일에 문제 있을시
                account_validate: 계정에 문제가 있을시
                False: 이미 존재하는 아이디로 고객 정보 생성시
                results: 고객 정보 생성 결과
            Author :
                taeha7b@gmail.com (김태하)
        """
        if name_validate(user_info.get('name')):
            return 'name_validate'
        elif birthday_validate(user_info.get('birthday')):
            return 'birthday_validate'
        elif account_validate(user_info.get('account')):
            return 'account_validate'
       
        existence_check = self.user_dao.account_checker(user_info, session)
        if existence_check['check'] == 1:
            return False
        results = self.user_dao.enroll_user(user_info, session)
        return results

    def user_list(self, page, session):
        """
            고객 정보 목록 조회(Business Layer)
            Args :
                page: 요청 받은 페이지 번호
                db : 데이터베이스 연결객체
            Returns :
                results: 고객 정보 목록
            Author :
                taeha7b@gmail.com (김태하)
        """
        page = int(page)-1
        pagination = {"page":page, "limit":2}
        results = self.user_dao.user_list(pagination, session)
        convert_results = []
        for user in results:
            id, account, name, birthday, memo = user
            convert_results.append({'id':id, 'account':account, 'name':name, 'birthday':birthday.strftime('%Y-%m-%d'), 'memo':memo})
        return convert_results

    def update_user(self, user_info, session):
        """
            고객 정보 변경(Business Layer)
            Args :
                user_info: 고객 데이터
                db : 데이터베이스 연결객체
            Returns :
                name_validate: 이름에 문제 발생시
                birthday_validate: 생년월일에 문제 있을시
                False: 이미 존재하는 아이디로 고객 정보 생성시
                results: 고객 정보 생성 결과
            Author :
                taeha7b@gmail.com (김태하)
        """
        if birthday_validate(user_info.get('birthday')):
            return 'birthday_validate'
        elif name_validate(user_info.get('name')):
            return 'name_validate'

        existence_check = self.user_dao.pk_checker(user_info, session)
        if existence_check['check'] == 0:
            return False
        results = self.user_dao.update_user(user_info, session)
        return results

    def delete_user(self, user_info, session):
        """
            고객 정보 삭제(Business Layer)
            Args :
                user_info: 고객 데이터
                db : 데이터베이스 연결객체
            Returns :
                account_validate: 계정에 문제가 있을시
                False: 이미 삭제된 아이디로 삭제 요청시
                results: 고객 정보 삭제 결과
            Author :
                taeha7b@gmail.com (김태하)
        """
        if account_validate(user_info.get('account')):
            return 'account_validate'

        existence_check = self.user_dao.account_checker(user_info, session)
        if existence_check['check'] == 0:
            return False
        results = self.user_dao.delete_user(user_info, session)
        return results

    def user_detail(self, account, session):
        """
            고객 정보 상세 조회(Business Layer)
            Args :
                account: 고객 아이디
                db : 데이터베이스 연결객체
            Returns :
                results: 고객 정보 상세 조회 결과
            Author :
                taeha7b@gmail.com (김태하)
        """
     
        results = self.user_dao.user_detail(account, session)
        id, account, name, birthday, memo = results
        convert_results = {'id':id, 'account':account, 'name':name, 'birthday':birthday.strftime('%Y-%m-%d'), 'memo':memo}
        return convert_results