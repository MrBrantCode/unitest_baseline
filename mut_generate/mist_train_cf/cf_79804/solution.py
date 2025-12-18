"""
QUESTION:
Write a function named `convert_timestamp(timestamp)` that takes an integer timestamp as input, converts it to a datetime object, and returns the result in the format "YYYY-MM-DD HH:MM:SS {Weekday}" where the weekday is in long format. The input timestamp is in seconds since the Unix epoch (January 1, 1970).
"""

from datetime import datetime

def convert_timestamp(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    custom_format = "%Y-%m-%d %H:%M:%S %A"
    return dt_object.strftime(custom_format)