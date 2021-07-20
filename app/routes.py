from app import db
from app.models.countdown_event import CountdownEvent
from app.models.user import User
from flask import request, Blueprint, make_response, jsonify

hello_world_bp = Blueprint("hello_world", __name__, url_prefix="/hello")

countdown_event_bp = Blueprint("countdown_event", __name__, url_prefix="/countdowns")
users_bp = Blueprint('user', __name__, url_prefix="/users")

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
        return jsonify(f"Countdown Event: {new_countdown.title} succesfully created."), 201

@countdown_event_bp.route("/<countdown_event_id>", methods=["GET", "PUT", "DELETE"])
def handle_countdown_event(countdown_event_id):
    countdown_event = CountdownEvent.query.get(countdown_event_id)

    if countdown_event is None:
        return make_response("", 404)

    if request.method == "GET":
        return {
            "id": countdown_event.id,
            "title": countdown_event.title,
            "timeTillEvent": countdown_event.countdown_till_date
        }
    elif request.method == "PUT":
        form_data = request.get_json()
        countdown_event.title = form_data["title"]
        countdown_event.countdown_till_date=["countdown_till_date"]
        db.session.commit()
        return make_response(f"Countdown Event: #{countdown_event.id} succesfully updated.")

    elif request.method == "DELETE":
        db.session.delete(countdown_event)
        db.session.commit()
        return make_response(f"Countdown Event: #{countdown_event.id} succesfully deleted.")

# `/users` will now return an empty array or array of user objects`
@users_bp.route("", methods=["GET", "POST"])
def handle_users():
    if request.method == "GET":
        users = User.query.all()
        print('users ----> ', users)

        users_response = []
        for user in users:
            users_response.append({
                "user_id": user.user_id,
                "creation_date": user.creation_date,
                "name": user.name
            })

        return jsonify(users_response)
    elif request.method == "POST":
        request_body = request.get_json()
        # need to add some attribute to hold something like a name for a user.
        new_user =  User(
            name=request_body["name"]
        )
        db.session.add(new_user)
        db.session.commit()

        return make_response({
            "user": {
                "user_id": new_user.user_id,
                "creation_date": new_user.creation_date,
                "name": new_user.name
            }
        }, 201)