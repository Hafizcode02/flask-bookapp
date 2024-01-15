from app import db_instance as db

class Users(db.Model):
    id = db.cloumn(db.Integer, primary_key=True, autoIncrement=True)
    name = db.column(db.string(255), nullable=False)
    email = db.column(db.string(255), nullable=False)
    password = db.column(db.string(255), nullable=False)
    is_active = db.column(db.Boolean, default=True)