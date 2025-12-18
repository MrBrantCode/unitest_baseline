"""
QUESTION:
Write a function `convert_to_hours_minutes(seconds)` that takes an integer number of seconds as input, converts it to minutes, and then to hours and minutes. The function should return the number of hours and minutes in the format that can be used to print "x hours and y minutes".
"""

def convert_to_hours_minutes(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    minutes %= 60

    return f"{hours} hours and {minutes} minutes"