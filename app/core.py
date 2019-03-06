from flask import Flask
from extensions import db, migrate, api
from config import Config


def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)

	api.init_app(app)
	db.init_app(app)
	migrate.init_app(app, db)

	return app