from flask_restx import Api
from flask import Blueprint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import render_template
from app.config import config_by_name

from logging.handlers import SMTPHandler
import logging

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

    ##Logger functionalities
    configure_logging(app)
    #logging.basicConfig(filename = 'Register.log', level=logging.DEBUG)

    ##Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('500.html'), 500
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
  

def configure_logging(app):
    # Eliminamos los posibles manejadores, si existen, del logger por defecto
    del app.logger.handlers[:]
    # Añadimos el logger por defecto a la lista de loggers
    loggers = [app.logger, ]
    handlers = []
    # Creamos un manejador para escribir los mensajes por consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(verbose_formatter())
    handlers.append(console_handler)
    # Asociamos cada uno de los handlers a cada uno de los loggers
    #if app.config['APP_ENV'] == app.config['APP_ENV_PRODUCTION']:
    console_handler.setLevel(logging.INFO)
    handlers.append(console_handler)
    mail_handler = SMTPHandler((app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                               app.config['DONT_REPLY_FROM_EMAIL'],
                               app.config['ADMINS'],
                               '[Error][{}] La aplicación falló'.format('DEBUG'),
                               (app.config['MAIL_USERNAME'],
                                app.config['MAIL_PASSWORD']),
                               ())
    mail_handler.setLevel(logging.DEBUG)
    mail_handler.setFormatter(mail_handler_formatter())
    handlers.append(mail_handler)

    for l in loggers:
        for handler in handlers:
            l.addHandler(handler)
        l.propagate = False
        l.setLevel(logging.DEBUG)

def verbose_formatter():
    return logging.Formatter(
        '[%(asctime)s.%(msecs)d] -- \t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )

def mail_handler_formatter():
    return logging.Formatter(
        '''
            Message type:       %(levelname)s
            Location:           %(pathname)s:%(lineno)d
            Module:             %(module)s
            Function:           %(funcName)s
            Time:               %(asctime)s.%(msecs)d
            Message:
            %(message)s
        ''',datefmt='%d/%m/%Y %H:%M:%S')