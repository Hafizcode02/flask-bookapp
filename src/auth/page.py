from flask import Blueprint, render_template, abort, request, redirect, url_for, session, flash, current_app
from jinja2 import TemplateNotFound
from database import db_instance as db
from src.models.users import Users

authPage = Blueprint('authPage', __name__,
                        template_folder='templates')

@authPage.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if all(request.form.get(key) is not None and request.form.get(key) != '' for key in ['email']):
            try:
                email = request.form.get('email')
                password = request.form.get('password')
            
                user = Users.query.filter_by(email=email).first()
            
                if not user or not user.check_password(password):
                    flash("Email or password is wrong")
                    return redirect(url_for('authPage.login'))
                
                session['loggedIn'] = True,
                session['userId'] = user.id,
                session['userName'] = user.name,
                
                return redirect(url_for('dashboardPage.dashboard'))
            
            except Exception as error:
                flash("Error : " + str(error))
                return redirect(url_for('authPage.login'))
            
        else:
            flash("All form must be filled")
            return redirect(url_for('authPage.login'))
        
    elif request.method == 'GET':
        return render_template('login.html')
    else:
        return "Method not allowed"
    
@authPage.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if all(request.form.get(key) is not None and request.form.get(key) != '' for key in ['name', 'email', 'password', 'password_confirmation']):
            if request.form.get('password') == request.form.get('password_confirmation'):
                try:
                    name = request.form.get('name')
                    email = request.form.get('email')
                    password = request.form.get('password')
                    
                    user = Users(name, email, password)
                    db.session.add(user)
                    db.session.commit()
                    
                    return redirect(url_for('authPage.login'))
                except Exception as error:
                    flash("Error : " + str(error))
                    return redirect(url_for('authPage.register'))
            else:
                flash("Password and password confirmation must be same")
                return redirect(url_for('authPage.register'))
        else:
            flash("All form must be filled")
            return redirect(url_for('authPage.register'))
        
    elif request.method == 'GET':
        return render_template('register.html')
    
@authPage.route("/logout")
def logout():
    session.pop('loggedIn', None)
    session.pop('userId', None)
    session.pop('userName', None)
    return redirect(url_for('authPage.login'))