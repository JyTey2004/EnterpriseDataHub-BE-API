# app/__init__.py
from flask import Flask
from config import db


def create_app():
    app = Flask(__name__)

    db_username = 'root'
    db_password = 'password$1'
    db_host = 'localhost'
    db_name = 'edh-mockdb'

    # Connection string for the MySQL database.
    connection_string = f'mysql://{db_username}:{db_password}@{db_host}/{db_name}'
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_string

    # Initialize the database with the app
    db.init_app(app)

    # Register the routes
    from app.routes.Super_Routes import routes_bp
    app.register_blueprint(routes_bp)

    return app
