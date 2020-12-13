import re


class AccountValidattionError(Exception):
    """
        유저 아이디 예외 발생
        Args:
            Exception : 예외 발생시의 메세지
        Author :
            taeha7b@gmail.com (김태하)
    """
    def __init__(self, message):
        super().__init__()
        self.message = message


def account_validate(value):
    """
        유저 아이디 유효성 검사 
        Args:
            유저 아이디
        Returns :
            True : 유저 아이디와 정규식이 일치하지 않으면 True를 반환함
        Author :
            taeha7b@gmail.com (김태하)
        History:
            2020-09-29 (taeha7b@gmail.com (김태하)) : 초기생성
    """
    regex = re.compile(r'^[a-zA-Z0-9]{4,12}$')
    if not regex.match(value):
        return True


class NameValidattionError(Exception):
    """
        유저 이름 예외 발생
        Args:
            Exception : 예외 발생시의 메세지
        Author :
            taeha7b@gmail.com (김태하)
    """
    def __init__(self, message):
        super().__init__()
        self.message = message


def name_validate(value):
    """
        유저 이름 유효성 검사 
        Args:
            유저 이름
        Returns :
            True : 유저 이름이 정규식이 일치하지 않으면 True를 반환함
        Author :
            taeha7b@gmail.com (김태하)
    """
    regex = re.compile(r'^[가-힣]{2,4}|^[a-zA-Z]{3,20}$')
    if not regex.match(value):
        return True

class BirthdayValidattionError(Exception):
    """
        유저 생년월일 예외 발생
        Args:
            Exception : 예외 발생시의 메세지
        Author :
            taeha7b@gmail.com (김태하)
    """
    def __init__(self, message):
        super().__init__()
        self.message = message


def birthday_validate(value):
    """
        유저 생년월일 유효성 검사 
        Args:
            유저 생년월일
        Returns :
            True : 유저의 생년월일이 정규식과 일치하지 않으면 True를 반환함
        Author :
            taeha7b@gmail.com (김태하)
    """
    regex = re.compile(r'^(19[0-9][0-9]|20\d{2})-(0[0-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$')
    if not regex.match(value):
        return True