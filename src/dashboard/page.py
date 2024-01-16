from flask import Blueprint, render_template, abort, session, redirect, url_for
from jinja2 import TemplateNotFound

dashboardPage = Blueprint('dashboardPage', __name__,
                        template_folder='templates')

@dashboardPage.route("/dashboard")
def dashboard():
    if 'loggedIn' in session and session['loggedIn'][0] == True:
        return render_template('dashboard.html', name=session['userName'][0])
    else:
        return redirect(url_for('authPage.login'))