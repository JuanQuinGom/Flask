from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, current_app

from app import db

from ..forms.forms import SignupForm
from app.user.services.auth_helper import Auth
from flask_restx import Api

bp_wtfv1 = Blueprint('wtfv1', __name__)
api = Api(bp_wtfv1)

posts = []

@bp_wtfv1.route("/")
def index():
    return render_template("admin/index.html", num_posts=len(posts))
@bp_wtfv1.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("admin/post_view.html", slug_title=slug)

@bp_wtfv1.route("/post/")
@bp_wtfv1.route("/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)

@bp_wtfv1.route("/signup_old/")
def show_signup_form():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		password = request.form['password']
		next = request.args.get('next', None)
		if next:
		    return redirect(next)
		return redirect(url_for('index'))
	return render_template("admin/signup_form.html")

@bp_wtfv1.route("/signup/", methods=["GET", "POST"])
def show_signupv2_form():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            data = request.form
            Auth.login_user(data)
            name = form.name.data
            email = form.email.data
            password = form.password.data
            current_app.logger.info(email)
            return redirect(url_for('wtfv1.index'))
    return render_template("admin/signup_form.html", form=form)

