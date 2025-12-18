"""
QUESTION:
Write a function named `get_day_of_week` that takes a string representing a date in the format DDMMYYYY and returns the day of the week corresponding to that date as a string.
"""

from datetime import datetime

def get_day_of_week(datestr):
    date = datetime.strptime(datestr, "%d%m%Y")
    return date.strftime('%A')