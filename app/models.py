import datetime
from extensions import db


class User(db.Model):
	__tablename__ = "User"


	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(35), unique=True, nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)
	password = db.Column(db.Strin(100), nullable=False)
	registration_date = db.Column(db.DateTime, default=datetime.datetime.now)


class Photo(db.Model):
	__tablename__ = "Photo"

	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	filename = db.Column(db.String(60), unique=True, nullable=False)
	created_date = db.Column(db.DateTime, default=datetime.datetime.now)
	description = db.Column(db.Text)
	
