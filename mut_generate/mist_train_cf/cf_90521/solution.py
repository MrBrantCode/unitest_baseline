"""
QUESTION:
Write a function `calculate_seconds(hours, minutes, seconds)` that takes three integers as input representing hours, minutes, and seconds. The function should return the total number of seconds. The input values must be non-negative integers, with a maximum value of 24 for hours and 60 for minutes and seconds. If the input values are invalid, the function should return an error message.
"""

def calculate_seconds(hours, minutes, seconds):
    if hours < 0 or minutes < 0 or seconds < 0:
        return "Input values must be non-negative integers."
    if hours > 24:
        return "Maximum value for hours is 24."
    if minutes > 60 or seconds > 60:
        return "Maximum value for minutes and seconds is 60."
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds