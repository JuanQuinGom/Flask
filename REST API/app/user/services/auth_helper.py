from app.user.models.user import User
from ..services.blacklist_service import save_token
from flask import current_app
import jwt
import json
class Auth:

    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            #current_app.logger.info(data.get('email'))
            #current_app.logger.info(data.get('password'))
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                #current_app.logger.info('Creating token')
                #current_app.logger.info(user.public_id)
                auth_token = User.encode_auth_token(user.public_id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                current_app.logger.info(response_object)
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
                'data' : user.public_id
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data
        else:
            auth_token = ''
        if auth_token:
            current_app.logger.debug(auth_token)
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403