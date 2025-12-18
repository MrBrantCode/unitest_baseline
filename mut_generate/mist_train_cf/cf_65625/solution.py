"""
QUESTION:
Design a function named `convert_unix_to_local` that takes an integer representing a Unix timestamp (in epoch time) as input and returns a string representing the corresponding local time and day of the week in the format "YYYY-MM-DD HH:MM:SS, Day". The function should use the system's local timezone.
"""

import time
import datetime

def convert_unix_to_local(unix_timestamp):
    # Convert the timestamp into a datetime object
    dt_object = datetime.datetime.fromtimestamp(unix_timestamp)

    # Format the datetime object into a string and get the day of the week
    formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S, %A')

    return formatted_time