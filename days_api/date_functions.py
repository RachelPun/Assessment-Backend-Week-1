"""Functions for working with dates."""

from datetime import datetime


def convert_to_datetime(date: str) -> datetime:
    """Converts string to datetime; returns datetime."""
    return datetime.strptime(date, "%d %m %Y")


def get_days_between(first: datetime, last: datetime) -> int:
    """Returns number of days between 2 dates."""
    pass


def get_day_of_week_on(date: datetime) -> str:
    """Returns the day of the week of a specific date."""
    pass
