from flask import Blueprint, render_template, redirect, url_for, session
from jinja2 import TemplateNotFound
from database import db_instance
from src.models.books import Books

bookPage = Blueprint('bookPage', __name__,
                        template_folder='templates')

@bookPage.before_request
def check_session():
    if 'loggedIn' not in session or session['loggedIn'][0] == False:
        return redirect(url_for('authPage.login'))

@bookPage.route("/book")
def book():
    bookData = db_instance.session.query(Books).all()
    return render_template('view/book/index.html', books=bookData)

@bookPage.route("/book/create")
def book_create():
    return render_template('view/book/create.html')

@bookPage.route("/book/store", methods=['POST'])
def book_store():
    return "OKE"

@bookPage.route("/book/edit/<id>")
def book_edit(id):
    return render_template('view/book/edit.html', id=id)

@bookPage.route("/book/update/<id>", methods=['POST'])
def book_update(id):
    return "OKE"

@bookPage.route("/book/delete/<id>")
def book_delete(id):
    return "OKE"