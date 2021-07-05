from flask import request, Blueprint, make_response, jsonify

hello_world_bp = Blueprint("hello_world", __name__, url_prefix="/hello")

@hello_world_bp.route("", methods=["GET"])
def hello_world():
    return 'Hello from Flask!'
# def endpoint_name():
