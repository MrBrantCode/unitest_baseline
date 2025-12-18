"""
QUESTION:
Write a function `get_weekday_and_time_elapsed` that takes a string representing an ISO 8601 date and timestamp, parses it into a date object, and returns the weekday of the date (where Monday is 0 and Sunday is 6) and the time elapsed since the start of the week (Monday 00:00:00) in minutes and seconds. The function should be able to handle different date and time formats.
"""

from datetime import datetime, timedelta
from dateutil import parser, tz

def get_weekday_and_time_elapsed(date_string):
    # Parse date string
    date = parser.parse(date_string)

    # Get weekday (Monday is 0 and Sunday is 6)
    weekday = date.weekday()

    # Get start of the week
    start_of_week = date - timedelta(days=weekday)

    # Get time elapsed since start of week
    elapsed = date - start_of_week.replace(hour=0, minute=0, second=0)

    # Get days, hours, minutes and seconds
    days, rem = divmod(elapsed.total_seconds(), 86400)
    hours, rem = divmod(rem, 3600)
    minutes, seconds = divmod(rem, 60)

    return weekday, int(days) * 24 * 60 + int(hours) * 60 + int(minutes), int(seconds)