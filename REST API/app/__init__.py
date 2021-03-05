from flask_restx import Api
from flask import Blueprint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from app.config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

from app.mod_auth.controllers import mod_auth as auth_module
from app.wtfv1.controller.wtfv1 import bp_wtfv1 as wtf_module
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    app.register_blueprint(auth_module, url_prefix='/auth2')
    app.register_blueprint(wtf_module, url_prefix='/wtf/1/')

    return app

from .user.controller.user_controller import api as user_ns
from .user.controller.auth_controller import api as auth_ns
from .products.controller.controllersProduct import api as products_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTX API',
          version='1.3',
          description='a boilerplate for flask restx web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(products_ns, path='/product')