"""
QUESTION:
Write a function `convert_minutes` that takes a positive integer `minutes` between 1 and 10000 as input and returns a string representing the equivalent time in the format "X hours and Y minutes". If the input is not a positive integer within the specified range, return an error message instead.
"""

def convert_minutes(minutes):
    if not isinstance(minutes, int) or minutes <= 0 or minutes > 10000:
        return "Invalid input. Please enter a positive integer between 1 and 10000."
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours} hours and {remaining_minutes} minutes"