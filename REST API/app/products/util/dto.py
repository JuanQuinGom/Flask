from flask_restplus import Namespace, fields


class ProductDto:
    api = Namespace('product', description='product related operations')
    product = api.model('product', {
        'product_name': fields.String(required=True, description='user email address'),
        'product_description': fields.String(required=True, description='user username'),
        'product_price': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='u1ser Identifier'),
        'registered_on': fields.Date(description = 'Date of creation')
    })