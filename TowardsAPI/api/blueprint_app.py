from flask import Flask

from blueprints_home import home_bp
from blueprints_contact import contact_bp

app = Flask(__name__)

app.register_blueprint(home_bp, url_prefix= '/home')
app.register_blueprint(contact_bp, url_prefix = '/contact')

app.run()