from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json(silent=True)
    if not data or "title" not in data:
        return jsonify({"error": "Request JSON must include a title."}), 400

    title = data["title"]
    next_id = max((event.id for event in events), default=0) + 1
    new_event = Event(next_id, title)
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201