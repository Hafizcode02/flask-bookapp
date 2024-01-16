from flask import Flask
from src.auth.page import authPage
from src.dashboard.page import dashboardPage
from src.book.page import bookPage
from flask_sqlalchemy import SQLAlchemy
from config import Config as config
from sqlalchemy.sql import text
from flask_session import Session

from database import db_instance

app = Flask(__name__)

# Configure session to use filesystem
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# db config
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config["SECRET_KEY"] = config.SECRET_KEY

db_instance.init_app(app)

app.register_blueprint(authPage)
app.register_blueprint(dashboardPage)
app.register_blueprint(bookPage)

@app.route("/testdb")
def testdb():
    try:
        db_instance.session.execute(text("SELECT 1")).all()
        return '<h1>It works.</h1>'
    except Exception as error:
        return '<h1>Something is broken.</h1> <br> Error : ' + str(error)

@app.route("/")
def index():
    return "Simple App with Flask, SQLAlchemy, Blueprints & Jinja2 <br> <a href='/login'>Login</a>"

if __name__ == "__main__":
    app.run(debug=True, host="localhost" , port=1500)