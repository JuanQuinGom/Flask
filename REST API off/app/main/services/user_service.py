import uuid
import datetime
from .. import flask_bcrypt
from app.main import db
from app.main.models.user import User
import sys
from flask import jsonify



def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password_hash=flask_bcrypt.generate_password_hash(data['password_hash']).decode('utf-8'),
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'password': flask_bcrypt.generate_password_hash(data['password_hash']).decode('utf-8')
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
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