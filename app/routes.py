from app import db
from app.models.countdown_event import CountdownEvent
from flask import request, Blueprint, make_response, jsonify

hello_world_bp = Blueprint("hello_world", __name__, url_prefix="/hello")

countdown_event_bp = Blueprint("countdown_event", __name__, url_prefix="/countdown")

@hello_world_bp.route("", methods=["GET"])
def hello_world():
    return 'Hello from Flask!'


@countdown_event_bp.route("", methods=["GET", "POST"])
def handle_countdown_events():
    if request.method == "GET":
        countdown_events = CountdownEvent.query.all()

        countdown_events_response = []
        for countdown in countdown_events:
            countdown_events_response.append({
                "id": countdown.id,
                "title": countdown.title,
                "countdown_till_date": countdown.countdown_till_date
            })
        return jsonify(countdown_events_response)

    elif request.method == "POST":
        request_body = request.get_json(request.data)

        if not "title" in request_body.keys()  or not "countdown_till_date" in request_body.keys():
            return make_response("", 422)

        new_countdown = CountdownEvent(
            title=request_body["title"],
            countdown_till_date=request_body["countdown_till_date"]
        )
        db.session.add(new_countdown)
        db.session.commit()
        return jsonify(f"Countdown Event:  {new_countdown.title} succesfully created."), 201