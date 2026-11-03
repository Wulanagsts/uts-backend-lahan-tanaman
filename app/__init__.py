
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)

    # Mendaftarkan Blueprint
    from app.routes.jenis_tanah_routes import jenis_tanah_bp
    from app.routes.jenis_tanaman_routes import jenis_tanaman_bp
    from app.routes.lahan_routes import lahan_bp
    from app.routes.tanaman_routes import tanaman_bp
    from app.routes.user_routes import user_bp
    from app.routes.advanced_routes import advanced_bp
    
    app.register_blueprint(jenis_tanah_bp)
    app.register_blueprint(jenis_tanaman_bp)
    app.register_blueprint(lahan_bp)
    app.register_blueprint(tanaman_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(advanced_bp)

    return app
