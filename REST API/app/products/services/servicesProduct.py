import uuid
import datetime
from app import db
from ..models.modelsProduct import Product
import sys
from flask import jsonify, current_app



def save_new_product(data):
    current_app.logger.info('Verificando...')
    product = Product.query.filter_by(product_name=data['product_name']).first()
    if not product:
        current_app.logger.info('Creando nuevo producto')
        new_product = Product(
            public_id=str(uuid.uuid4()),
            product_name = data['product_name'],
            product_description = data['product_description'],
            product_price = int(data['product_price']),
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_product)
        response_object = {
            'status': 'success',
            'message': 'Product successfully registered.',
        }
        return response_object, 201
    else:
        current_app.logger.info('Producto existente')
        response_object = {
            'status': 'fail',
            'message': 'Product already exists.',
        }
        return response_object, 409


def get_all_products():
    return Product.query.all()


def get_a_product(public_id):
    return Product.query.filter_by(public_id=public_id).first()

def delete_a_product(public_id):
    product = Product.query.filter_by(public_id=public_id).first()
    if not product:
        response_object = {
        'status':'Fail',
        'message': 'Product not found, retry using another id'
        }
        return response_object, 404
    else:
        delete_changes(product)
        response_object = {
        'status': 'Success',
        'message': 'Product deleted successfully'
        }
        return response_object, 200

def modify_product(data, public_id):
    product = Product.query.filter_by(public_id=public_id).first()
    if product:
        modified_product = Product(
            public_id=str(product.public_id),
            product_name = data['product_name'],
            product_description = data['product_description'],
            product_price = int(data['product_price']),
            registered_on=datetime.datetime.utcnow()
        )
        delete_changes(product)
        save_changes(modified_product)
        response_object = {
            'status': 'success',
            'message': 'Successfully modified.',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Product does not exists. Modify ID.',
        }
        return response_object, 404


def save_changes(data):
    #lo adiciona y guarda en la BD
    db.session.add(data)
    db.session.commit()

def delete_changes(data):
    db.session.delete(data)
    db.session.commit()
