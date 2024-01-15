from flask import Blueprint, render_template, abort, request, redirect, url_for, session, flash
from jinja2 import TemplateNotFound

authPage = Blueprint('authPage', __name__,
                        template_folder='templates')

@authPage.route("/login")
def login():
    return render_template('login.html')
    
@authPage.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if all(request.form.get(key) is not None and request.form.get(key) != '' for key in ['name', 'email', 'password', 'password_confirmation']):
            if request.form.get('password') == request.form.get('password_confirmation'):
                # return "HOLA"
                return redirect(url_for('authPage.login'))
                # try:
                #     name = request.form.get('name')
                #     email = request.form.get('email')
                #     password = request.form.get('password')
                    
                #     user = Users(name, email, password)
                #     db.session.add(user)
                    
                #     return redirect(url_for('authPage.login'))
                # except Exception as error:
                #     flash("Error : " + str(error))
                #     return redirect(url_for('authPage.register'))
            else:
                flash("Password and password confirmation must be same")
                return redirect(url_for('authPage.register'))
        else:
            flash("All form must be filled")
            return redirect(url_for('authPage.register'))
        
    elif request.method == 'GET':
        return render_template('register.html')