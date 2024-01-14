from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Halo dari Halaman Index"

# @app.route('/login', methods=['GET', 'POST'])
@app.route("/login")
def login():
    # if request.method == 'POST':
    #     return 'Ini adalah method POST'
    # elif request.method == 'GET':
    return render_template('login.html')
    # else:
    #     return 'Method Not Allowed'
    
@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/book")
def book():
    return render_template('view/book/index.html')

@app.route("/book/create")
def book_create():
    return render_template('view/book/create.html')

@app.route("/book/edit/<id>")
def book_edit():
    return render_template('view/book/edit.html', id=id)

if __name__ == "__main__":
    app.run(debug=True)