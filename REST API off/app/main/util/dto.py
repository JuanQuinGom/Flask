from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password_hash': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='u1ser Identifier'),
        'registered_on': fields.Date(description = 'Date of creation')
    })