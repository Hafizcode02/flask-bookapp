from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

authPage = Blueprint('authPage', __name__,
                        template_folder='templates')

@authPage.route("/login")
def login():
    return render_template('login.html')
    
@authPage.route("/register")
def register():
    return render_template('register.html')