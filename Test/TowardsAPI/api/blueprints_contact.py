from flask import Blueprint

contact_bp=Blueprint('contact',__name__)

@contact_bp.route('/hello/')
def hello_contact():
	return "Hello from contact page"