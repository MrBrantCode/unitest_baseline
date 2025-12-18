"""
QUESTION:
Write a Python function `get_day_of_week` that takes a DateTime string in ISO format as input and returns the day of the week corresponding to the given date. The function should use the `datetime` module to convert the input string to a `datetime` object and output the full name of the day of the week.
"""

from datetime import datetime

def get_day_of_week(dt_string):
    """Return the day of the week corresponding to the given DateTime string."""
    dt_object = datetime.fromisoformat(dt_string)
    return dt_object.strftime("%A")