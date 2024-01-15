from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bookPage = Blueprint('bookPage', __name__,
                        template_folder='templates')

@bookPage.route("/book")
def book():
    return render_template('view/book/index.html')

@bookPage.route("/book/create")
def book_create():
    return render_template('view/book/create.html')

@bookPage.route("/book/edit/<id>")
def book_edit(id):
    return render_template('view/book/edit.html', id=id)