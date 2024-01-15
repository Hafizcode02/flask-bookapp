from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

dashboardPage = Blueprint('dashboardPage', __name__,
                        template_folder='templates')

@dashboardPage.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')