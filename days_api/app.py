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
def history_get_or_delete():
    """Returns details on the last number of requests to the API."""
    pass


@app.route("/between", methods=["POST"])
def post_days_between_dates():
    """Returns the number of days between two dates."""
    pass


@app.route("/weekday", methods=["POST"])
def post_weekday_of_date():
    """Returns the day of the week a specific date is."""
    pass


if __name__ == "__main__":
    app.run(port=8080, debug=True)
