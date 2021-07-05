# from app.models import countdown_event
from flask import request, Blueprint, make_response, jsonify

hello_world_bp = Blueprint("hello_world", __name__, url_prefix="/hello")

countdown_event_bp = Blueprint("countdown_event", __name__, url_prefix="/countdown")

@hello_world_bp.route("", methods=["GET"])
def hello_world():
    return 'Hello from Flask!'


@countdown_event_bp.route("", methods=["GET"])
def handle_countdown_events():
    return "handling countdown event"
