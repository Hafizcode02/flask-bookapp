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

if __name__ == "__main__":
    app.run(debug=True)