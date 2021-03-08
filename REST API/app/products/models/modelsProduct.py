from app import db

import datetime
import jwt
from app.config import key

class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(255), unique=True, nullable=False)
    product_description = db.Column(db.String(255), nullable=False)
    product_price = db.Column(db.Integer, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    public_id = db.Column(db.String(100), unique=True)

    def __init__(self, product_name, product_description, product_price, public_id, registered_on):
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.public_id = public_id
        self.registered_on = registered_on

    def __repr__(self):
        return "<User '{}'>".format(self.product_name)