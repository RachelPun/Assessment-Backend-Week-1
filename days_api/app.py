"""This file defines the API routes."""

# pylint: disable = no-name-in-module

from datetime import datetime

from flask import Flask, Response, request, jsonify

from date_functions import convert_to_datetime, get_day_of_week_on, get_days_between

app_history = []

app = Flask(__name__)


def add_to_history(current_request):
    """Adds a route to the app history."""
    app_history.append({
        "method": current_request.method,
        "at": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "route": current_request.endpoint
    })


@app.get("/")
def index():
    """Returns an API welcome messsage."""
    return jsonify({"message": "Welcome to the Days API."})


@app.route("/history", methods=["GET", "DELETE"])
def history():
    """Returns details on the last number of requests to the API."""

    if request.method == "GET":
        num = 5
        if "number" in request.args:
            if not request.args["number"].isnumeric():
                return jsonify({"error": "Number must be an integer between 1 and 20."}), 400
            if not 1 <= int(request.args["number"]) <= 20:
                return jsonify({"error": "Number must be an integer between 1 and 20."}), 400
            num = int(request.args["number"])

        add_to_history(request)
        return jsonify(app_history[-1:-num:-1])

    if request.method == "DELETE":
        app_history.clear()
        add_to_history(request)
        return jsonify({"status": "History cleared"})


@app.route("/between", methods=["POST"])
def post_days_between_dates():
    """Returns the number of days between two dates."""

    if not all(arg in request.json for arg in ["first", "last"]):
        return jsonify({"error": "Missing required data."}), 400

    try:
        first = convert_to_datetime(request.json["first"])
        last = convert_to_datetime(request.json["last"])
    except Exception as error:
        return jsonify({"error": error.args[0]}), 400

    days = get_days_between(first, last)

    add_to_history(request)
    return jsonify({"days": days})


@app.route("/weekday", methods=["POST"])
def post_weekday_of_date():
    """Returns the day of the week a specific date is."""

    if "date" not in request.json:
        return jsonify({"error": "Missing required data."}), 400

    try:
        date = convert_to_datetime(request.json["date"])
    except Exception as error:
        return jsonify({"error": error.args[0]}), 400

    day = get_day_of_week_on(date)

    add_to_history(request)
    return jsonify({"weekday": day})


if __name__ == "__main__":
    app.run(port=8080, debug=True)
