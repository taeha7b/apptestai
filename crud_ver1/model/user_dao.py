class UserDao:
    def enroll_user(self, user_info, db): 
        with db.cursor() as cursor: 
            sql_1 = """ 
            INSERT INTO users (
                account
            ) VALUES(%s)
            """
            results_1 = cursor.execute(sql_1,user_info['account'])
            lastrowid = cursor.lastrowid
            sql_2 = """
            INSERT INTO user_details (
            user_id,
            name,
            birthday,
            memo
            ) VALUES (%s,%s,%s,%s)
            """
            results_2 = cursor.execute(sql_2, 
                (
                    lastrowid,
                    user_info['name'],
                    user_info['birthday'],
                    user_info['memo']
                )
            )
            return results_2

    def user_list(self, pagination, db):
        with db.cursor() as cursor:
            sql = """ 
            SELECT u.id, u.account, ud.name, ud.birthday, ud.memo 
            FROM users as u INNER JOIN user_details as ud 
            ON u.id = ud.user_id LIMIT %s OFFSET %s;
            """
            cursor.execute(sql,(
                pagination['limit'],
                pagination['limit']*pagination['page']
                ))
            results = cursor.fetchall()
            return results

    def user_detail(self, account, db):
        with db.cursor() as cursor:
            sql = """ 
            SELECT u.id, u.account, ud.name, ud.birthday, ud.memo 
            FROM users as u INNER JOIN user_details as ud 
            ON u.id = ud.user_id 
            AND u.account = %s;
            """
            cursor.execute(sql, account)
            results = cursor.fetchone()
            return results

    def update_user(self, user_info, db): 
        with db.cursor() as cursor: 
            sql = """
            UPDATE user_details SET
            name = %s,
            birthday = %s,
            memo = %s
            WHERE user_id = %s
            """
            results = cursor.execute(sql, 
                (   
                    user_info['name'],
                    user_info['birthday'],
                    user_info['memo'],
                    user_info['id']
                )
            )
            return results

    def delete_user(self, user_info, db): 
        with db.cursor() as cursor: 
            sql = """ 
            DELETE FROM users WHERE account = %s
            """
            results = cursor.execute(sql,user_info['account'])
            return results


            