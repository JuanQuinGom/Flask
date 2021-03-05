from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password_hash': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='u1ser Identifier'),
        'registered_on': fields.Date(description = 'Date of creation')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class TokenDto:
    api = Namespace('token', description='Authentication related operations')
    token_auth = api.model('auth_details', {
        'token': fields.String(required=True, description='The user password '),
    })