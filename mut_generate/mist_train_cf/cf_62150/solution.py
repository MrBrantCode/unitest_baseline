"""
QUESTION:
Write a function `convert_to_military_time(time_string)` that takes a time string in 12-hour format (HH:MM:SS AM/PM) and returns the equivalent time in 24-hour format (HH:MM:SS).
"""

from datetime import datetime

def convert_to_military_time(time_string):
    time_object = datetime.strptime(time_string, '%I:%M:%S %p')
    return time_object.strftime('%H:%M:%S')