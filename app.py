from flask import Flask, render_template
from src.auth.page import authPage
from src.dashboard.page import dashboardPage
from src.book.page import bookPage

app = Flask(__name__)

app.register_blueprint(authPage)
app.register_blueprint(dashboardPage)
app.register_blueprint(bookPage)

@app.route("/")
def index():
    return "Simple App with Flask, SQLAlchemy, Blueprints & Jinja2 <br> <a href='/login'>Login</a>"

if __name__ == "__main__":
    app.run(debug=True, host="localhost" , port=1500)