from flask import Blueprint, render_template, abort, session, redirect, url_for
from jinja2 import TemplateNotFound

dashboardPage = Blueprint('dashboardPage', __name__,
                        template_folder='templates')

@dashboardPage.before_request
def check_session():
    if 'loggedIn' not in session or session['loggedIn'][0] == False:
        return redirect(url_for('authPage.login'))

@dashboardPage.route("/dashboard")
def dashboard():
    return render_template('dashboard.html', name=session['userName'][0])