"""
QUESTION:
Write a function named `convert_time` that takes a string `user_time` in 12-hour time format (HH:MM:SS AM/PM) and returns the equivalent time in 24-hour format (HH:MM:SS). The function should raise an error message if the input time string is invalid (non-numeric or out-of-range values).
"""

from datetime import datetime

def convert_time(user_time):
    try:
        # check if the input time is in correct format
        time_object = datetime.strptime(user_time, "%I:%M:%S %p")

        # convert to 24-hour format
        military_time = datetime.strftime(time_object, "%H:%M:%S")
        
        return military_time
    except ValueError:
        return "Invalid input. Please input time in 12-hour format (HH:MM:SS AM/PM)"