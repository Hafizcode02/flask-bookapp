from flask import Blueprint, render_template, redirect, url_for, session, request, flash
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
    if all(request.form.get(key) is not None and request.form.get(key) != '' for key in ['judul', 'penulis', 'penerbit', 'tahun_terbit']):
        try:
            judul = request.form.get('judul')
            penulis = request.form.get('penulis')
            penerbit = request.form.get('penerbit')
            tahun_terbit = request.form.get('tahun_terbit')
            
            book = Books(judul, penulis, penerbit, tahun_terbit)
            db_instance.session.add(book)
            db_instance.session.commit()
            
            flash("Book has been created")
            return redirect(url_for('bookPage.book'))
        except Exception as error:
            flash("Error : " + str(error))
            return redirect(url_for('bookPage.book_create'))
    else:
        flash("All form must be filled")
        return redirect(url_for('bookPage.book_create'))

@bookPage.route("/book/edit/<id>")
def book_edit(id):
    book  = Books.query.get(id)
    return render_template('view/book/edit.html', book=book)

@bookPage.route("/book/update/<id>", methods=['POST'])
def book_update(id):
    if all(request.form.get(key) is not None and request.form.get(key) != '' for key in ['judul', 'penulis', 'penerbit', 'tahun_terbit']):
        try:
            book  = Books.query.get(id)
            book.judul = request.form.get('judul')
            book.penulis = request.form.get('penulis')
            book.penerbit = request.form.get('penerbit')
            book.tahun_terbit = request.form.get('tahun_terbit')
            
            db_instance.session.commit()
            
            flash("Book has been updated")
            return redirect(url_for('bookPage.book'))
        except Exception as error:
            flash("Error : " + str(error))
            return redirect(url_for('bookPage.book'))
    else:
        flash("All form must be filled")
        return redirect(url_for('bookPage.book_update', id=id))

@bookPage.route("/book/delete/<id>")
def book_delete(id):
    return "OKE"