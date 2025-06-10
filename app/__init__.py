from flask import Flask
from app.utils.db import init_db
from app.routes.auth_routes import auth_bp
from app.routes.client_routes import client_bp
from app.config import Config

def create_app():
    app = Flask(__name__)
    config = Config()
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['DB_PATH'] = config.DB_PATH

    # Inicializar la BD
    init_db(app)

    # Registrar Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(client_bp)

    return app
