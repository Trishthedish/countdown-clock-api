from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI"
        )
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI"
        )
    
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.countdown_event import CountdownEvent
    from .routes import countdown_event_bp
    app.register_blueprint(countdown_event_bp)

    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    CORS(app)
    return app