class UserDao:
    def enroll_user(self, user_info, session): 
        """
            고객 정보 생성(Persistence Layer)
            Args :
                user_info: 고객 데이터
                session : 데이터베이스 연결객체
            Returns :
                results_2: 고객 정보 생성 결과
            Author :
                taeha7b@gmail.com (김태하)
        """
       
        sql_1 = """ 
            INSERT INTO users (
                account
            ) VALUES(%s)
            """
        lastrowid = session.bind.execute(sql_1,user_info['account']).lastrowid
        sql_2 = """
            INSERT INTO user_details (
            user_id,
            name,
            birthday,
            memo
            ) VALUES (%s,%s,%s,%s)
            """
        results = session.bind.execute(sql_2, 
                (
                    lastrowid,
                    user_info['name'],
                    user_info['birthday'],
                    user_info['memo']
                )
            )
        return results

    def user_list(self, pagination, session):
        """
            고객 정보 목록 조회(Persistence Layer)
            Args :
                pagination: LIMIT와 OFFSET가 있는 딕셔너리
                session : 데이터베이스 연결객체
            Returns :
                results: 고객 정보 목록 조회 결과
            Author :
                taeha7b@gmail.com (김태하)
        """
        sql = """ 
            SELECT u.id, u.account, ud.name, ud.birthday, ud.memo 
            FROM users as u INNER JOIN user_details as ud 
            ON u.id = ud.user_id LIMIT %s OFFSET %s;
        """
        results = session.bind.execute(sql,(
            pagination['limit'],
            pagination['limit']*pagination['page']
            )).fetchall()
        return results

    def user_detail(self, account, session):
        """
            고객 정보 상세 조회(Persistence Layer)
            Args :
                account: 유저의 아이디
                session : 데이터베이스 연결객체
            Returns :
                results: 고객 정보 상세 조회 결과
            Author :
                taeha7b@gmail.com (김태하)
        """
  
        sql = """ 
            SELECT u.id, u.account, ud.name, ud.birthday, ud.memo 
            FROM users as u INNER JOIN user_details as ud 
            ON u.id = ud.user_id 
            AND u.account = %s;
        """
        
        results = session.bind.execute(sql, account).fetchone()
        return results

    def update_user(self, user_info, session):
        """
            고객 정보 변경(Persistence Layer)
             Args :
                user_info: 유저의 아이디
                session : 데이터베이스 연결객체
            Returns :
                results: 고객 정보 변경 결과
            Author :
                taeha7b@gmail.com (김태하)
        """
       
        sql = """
            UPDATE user_details SET
            name = %s,
            birthday = %s,
            memo = %s
            WHERE user_id = %s
            """
        results = session.bind.execute(sql, 
            (   
                user_info['name'],
                user_info['birthday'],
                user_info['memo'],
                user_info['id']
            )
        )
        return results

    def delete_user(self, user_info, session):
        """
            고객 정보 삭제(Persistence Layer)
             Args :
                user_info: 유저의 아이디
                session : 데이터베이스 연결객체
            Returns :
                results: 고객 정보 삭제 결과
            Author :
                taeha7b@gmail.com (김태하)
        """
      
        sql = """ 
            DELETE FROM users WHERE account = %s
        """
        results = session.bind.execute(sql,user_info['account'])
        return results

    def account_checker(self, user_info, session):
        """
            아이디 확인(Persistence Layer)
             Args :
                user_info: 유저의 아이디
                session : 데이터베이스 연결객체
            Returns :
                results: 아이디 확인 결과값 
                        아이디가 일을시: {"check":1} 
                        아이디가 없을시: {"check":0}
            Author :
                taeha7b@gmail.com (김태하)
        """
       
        sql = """ 
            SELECT EXISTS (
                SELECT account 
                FROM users 
                WHERE account = %s) 
                as 'check'
            """
        results = session.bind.execute(sql, user_info['account']).fetchone()
        return results

    def pk_checker(self, user_info, session):
        """
            고유키 확인(Persistence Layer)
            Args :
                user_info: 유저의 아이디
                session : 데이터베이스 연결객체
            Returns :
                results: 아이디 확인 결과값 
                        아이디가 일을시: {"check":1} 
                        아이디가 없을시: {"check":0}
            Author :
                taeha7b@gmail.com (김태하)
        """
         
        sql = """ 
            SELECT EXISTS (
                SELECT account 
                FROM users 
                WHERE id = %s) 
                as 'check'
            """
        results = session.bind.execute(sql, user_info['id']).fetchone()
        return results