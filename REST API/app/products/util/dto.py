from flask_restx import Namespace, fields


class ProductDto:
    api = Namespace('product', description='product related operations')
    product = api.model('product', {
        'product_name': fields.String(required=True, description='name of the product'),
       'product_description': fields.String(required=True, description='description of the prod'),
        'product_price': fields.Integer(required=True, description='price of the product'),
        'public_id': fields.String(description='u1ser Identifier'),
        'registered_on': fields.Date(description = 'Date of creation')
    })