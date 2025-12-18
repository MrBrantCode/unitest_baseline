"""
QUESTION:
Write a function `convert_hours_to_hours_and_minutes(hours)` that takes a floating-point number of hours as input, converts it to minutes, then converts the minutes back to hours and minutes. The result should be in the format "x hours and y minutes" and rounded to the nearest minute.
"""

import math

def entrance(hours):
    minutes = hours * 60
    hours = math.floor(minutes / 60)
    remaining_minutes = round(minutes % 60)
    return f"{hours} hours and {remaining_minutes} minutes"