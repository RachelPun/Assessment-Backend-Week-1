"""Functions for working with dates."""

from datetime import datetime


def convert_to_datetime(date: str) -> datetime:
    """Converts string to datetime; returns datetime."""
    try:
        return datetime.strptime(date, "%d.%m.%Y")
    except:
        raise ValueError("Unable to convert value to datetime.")


def get_days_between(first: datetime, last: datetime) -> int:
    """Returns number of days between 2 dates."""

    if not all(isinstance(arg, datetime) for arg in [first, last]):
        raise TypeError("Datetimes required.")

    delta = last - first
    return delta.days


def get_day_of_week_on(date: datetime) -> str:
    """Returns the day of the week of a specific date."""

    if not isinstance(date, datetime):
        raise TypeError("Datetime required.")

    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = date.timetuple()[6]
    return days[day_index]
