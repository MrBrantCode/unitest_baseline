"""
QUESTION:
Write a function `convert_date(date_string)` that takes a string representing a date in various formats as input and returns the date in the standardized ISO 8601 format (YYYY-MM-DD). The function should discard the day of the week and validate the date, returning an error message if the date is invalid.
"""

from dateutil import parser
from datetime import datetime

def convert_date(date_string):
    try:
        dt = parser.parse(date_string)
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        return "Invalid date"