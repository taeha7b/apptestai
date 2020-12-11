import datetime

class UserService:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def enroll_user(self, user_info, db):
        results = self.user_dao.enroll_user(user_info, db)
        return results

    def user_list(self, page, db):
        page = int(page)-1
        pagination = {"page":page, "limit":2}
        results = self.user_dao.user_list(pagination, db)
        for user in results:
            user['birthday'] = user['birthday'].strftime('%Y-%m-%d')
        return results

    def update_user(self, user_info, db):
        results = self.user_dao.update_user(user_info, db)
        return results

    def delete_user(self, user_info, db):
        results = self.user_dao.delete_user(user_info, db)
        return results

    def user_detail(self, account, db):
        results = self.user_dao.user_detail(account, db)
        results['birthday'] = results['birthday'].strftime('%Y-%m-%d')
        return results
