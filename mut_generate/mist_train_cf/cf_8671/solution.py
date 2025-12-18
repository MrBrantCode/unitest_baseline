"""
QUESTION:
Write a function `calculate_seconds(hours, minutes, seconds)` that takes three non-negative integers as input, calculates the total number of seconds, and returns the result. The function should return an error message if any of the input values are negative or exceed their maximum values (24 for hours, 60 for minutes, 60 for seconds).
"""

def calculate_seconds(hours, minutes, seconds):
    if hours < 0 or minutes < 0 or seconds < 0:
        return "Input values must be non-negative integers."
    if hours > 23 or minutes > 59 or seconds > 59:
        return "Invalid time."
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds