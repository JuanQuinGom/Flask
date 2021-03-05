import uuid
import datetime
from app import flask_bcrypt
from app import db
from app.user.models.user import User
import sys
from flask import jsonify, current_app, request



def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        current_app.logger.info('Creando nuevo producto')
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password_hash=flask_bcrypt.generate_password_hash(data['password_hash']).decode('utf-8'),
            registered_on=datetime.datetime.utcnow()
        )
        #save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'password': new_user.password_hash
        }
        current_app.logger.debug('Generando token')
        return generate_token(new_user)
        #return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    """
    current_app.logger.info('Metodo')
    current_app.logger.info(request.method)
    current_app.logger.info('Ruta')
    current_app.logger.info(request.path)
    current_app.logger.info('headers')
    """
    #current_app.logger.info(request.mimetype)
    current_app.logger.info(request.content_type)
    #current_app.logger.info(request.args)
    #current_app.logger.info(request.json)
    #current_app.logger.info(request.headers)

    return User.query.all()


def get_a_user(public_id):
    current_app.logger.info(request.path)
    current_app.logger.info(request.headers)
    return User.query.filter_by(public_id=public_id).first()

def delete_a_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        response_object = {
        'status':'Fail',
        'message': 'User not found, retry using another id'
        }
        return response_object, 404
    else:
        delete_changes(user)
        response_object = {
        'status': 'Success',
        'message': 'User deleted successfully'
        }
        return response_object, 200

def modify_users(data, public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if user:
        modified_user = User(
            public_id=str(user.public_id),
            email=data['email'],
            username=data['username'],
            password_hash=flask_bcrypt.generate_password_hash(data['password_hash']).decode('utf-8'),
            registered_on=datetime.datetime.utcnow()
        )
        delete_changes(user)
        save_changes(modified_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully modified.',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User does not exists. Modify ID.',
        }
        return response_object, 404


def save_changes(data):
    #lo adiciona y guarda en la BD
    db.session.add(data)
    db.session.commit()

def delete_changes(data):
    db.session.delete(data)
    db.session.commit()

def generate_token(user):
    try:
        # generate the auth token
        #current_app.logger.debug(user.public_id)
        auth_token = User.encode_auth_token(user.public_id)
        #current_app.logger.debug(auth_token)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token,
            #'password': user.password_hash
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401