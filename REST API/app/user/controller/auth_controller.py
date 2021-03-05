from flask import request, current_app
from flask_restx import Resource

from app.user.services.auth_helper import Auth
from ..util.dto import AuthDto, TokenDto

api = AuthDto.api
user_auth = AuthDto.user_auth
token_auth = TokenDto.token_auth

@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        """Login test using an email and password"""
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        """Logout option (testing)"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        current_app.logger.debug(auth_header)
        return Auth.logout_user(data=auth_header)