from flask import request, Blueprint, current_app
from flask_restx import Resource


from ..util.dto import ProductDto
from ..services.servicesProduct import save_new_product, get_all_products, get_a_product, delete_a_product, modify_product

from ..models.modelsProduct import Product

api = ProductDto.api
_product = ProductDto.product

product_bp = api

@product_bp.route('/')
class ProductList(Resource):
    

    @product_bp.doc('list_of_registered_products')
    @product_bp.marshal_list_with(_product, envelope='data')
    
    def get(self):
        """List all registered products"""
        return get_all_products()

    @product_bp.response(201, 'Product successfully created.')
    

    @product_bp.doc('create a new product')
    @product_bp.expect(_product, validate=True)
    
    def post(self):
        """Creates a new product """
        data = request.json
        return save_new_product(data=data)


@product_bp.route('/<public_id>')
@product_bp.param('public_id', 'The product identifier')
@product_bp.response(404, 'Product not found.')
class Product(Resource):
    @product_bp.doc('get a product')
    @product_bp.marshal_with(_product)
    def get(self, public_id):
        """get a product given its identifier"""
        product = get_a_product(public_id)
        if not product:
            product_bp.abort(404)
        else:
            return product
    def delete(self, public_id):
        """delete a product via its id"""
        product = delete_a_product(public_id)
        if not product:
            product_bp.abort(404)
        else:
            return product
    
    @product_bp.expect(_product, validate=True)
    def put(self, public_id):
        """modify a product via its id"""
        data = request.json
        return modify_product(data = data, public_id= public_id)
