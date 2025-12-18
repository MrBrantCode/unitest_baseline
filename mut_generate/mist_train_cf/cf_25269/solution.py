"""
QUESTION:
Convert a given date string in the format "YYYY-MM-DD HH:MM:SS" to a timestamp. Implement the function `convert_to_timestamp` that takes a date string as input and returns the corresponding timestamp.
"""

import datetime

def convert_to_timestamp(date_string):
    """Write a code to convert a given date string into a timestamp."""
    date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    timestamp = datetime.datetime.timestamp(date_object)
    return timestamp