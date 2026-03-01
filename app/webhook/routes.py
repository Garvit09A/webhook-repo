from flask import Blueprint, json, request
from datetime import datetime
from app.extensions import collection
from flask import request, jsonify

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route("/receiver", methods=["POST"])
def webhook_receiver():
    data = request.json
    event_type = request.headers.get("X-GitHub-Event")

    event_data = {}

    if event_type == "push":
        event_data = {
            "type": "push",
            "author": data["pusher"]["name"],
            "to_branch": data["ref"].split("/")[-1],
            "timestamp": datetime.utcnow()
        }

    elif event_type == "pull_request":
        if data["action"] == "opened":
            event_data = {
                "type": "pull_request",
                "author": data["pull_request"]["user"]["login"],
                "from_branch": data["pull_request"]["head"]["ref"],
                "to_branch": data["pull_request"]["base"]["ref"],
                "timestamp": datetime.utcnow()
            }

        elif data["action"] == "closed" and data["pull_request"]["merged"]:
            event_data = {
                "type": "merge",
                "author": data["pull_request"]["user"]["login"],
                "from_branch": data["pull_request"]["head"]["ref"],
                "to_branch": data["pull_request"]["base"]["ref"],
                "timestamp": datetime.utcnow()
            }

    if event_data:
        collection.insert_one(event_data)

    return jsonify({"status": "success"})
@webhook.route("/events", methods=["GET"])
def get_events():
    events = list(collection.find().sort("timestamp", -1).limit(10))

    for event in events:
        event["_id"] = str(event["_id"])
        event["timestamp"] = event["timestamp"].strftime("%d %B %Y - %I:%M %p UTC")

    return jsonify(events)