from flask import Flask
from .routes import main_bp
from .config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(main_bp)

    return app
