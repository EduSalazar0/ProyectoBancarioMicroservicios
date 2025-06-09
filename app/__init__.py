from flask import Flask
from app.config import Config
from app.utils.db import init_db

def create_app():
    app = Flask(__name__)
    config = Config()
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['DB_PATH'] = config.DB_PATH

    init_db(app)
    
    # Registrar Blueprints
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    return app
