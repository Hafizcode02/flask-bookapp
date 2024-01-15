from app import db_instance as db

class Books(db.Model):
    id = db.cloumn(db.Integer, primary_key=True, autoIncrement=True)
    judul = db.column(db.string(255), nullable=False)
    penulis = db.column(db.string(255), nullable=False)
    penerbit = db.column(db.string(255), nullable=False)
    tahun_terbit = db.column(db.string(10), nullable=False)