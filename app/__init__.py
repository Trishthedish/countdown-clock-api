from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
# load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)

    return app
    
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.countdown_event import CountdownEvent

    from .routes import countdown_events_bp
    app.register_blueprint(countdown_events_bp)

    return app