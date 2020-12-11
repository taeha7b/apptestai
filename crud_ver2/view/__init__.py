from .user_view import (
    UserMgmt,
    UserDetail
    )

def create_endpoints(app, services):
    user_service = services.user_service

    app.add_url_rule('/users', view_func = UserMgmt.as_view('user_mgmt', user_service))
    app.add_url_rule('/user-detail/<string:account>', view_func = UserDetail.as_view('user_detail', user_service))