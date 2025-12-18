"""
QUESTION:
Write a Python function `time_diff` that calculates the difference between two times given in 24-hour format and translates this difference into hours, minutes, and seconds. The function takes two time strings in the format `HH:MM:SS` as input and returns the time difference as a tuple of three integers representing hours, minutes, and seconds. Assume that the first time is always earlier than the second time.
"""

from datetime import datetime

def time_diff(time1, time2):
    format_str = "%H:%M:%S" 
    datetime_obj1 = datetime.strptime(time1, format_str)
    datetime_obj2 = datetime.strptime(time2, format_str)
    diff = datetime_obj2 - datetime_obj1

    hours = diff.seconds // 3600
    minutes = (diff.seconds // 60) % 60
    seconds = diff.seconds % 60

    return hours, minutes, seconds