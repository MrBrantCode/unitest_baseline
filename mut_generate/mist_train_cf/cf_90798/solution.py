"""
QUESTION:
Create a function named `time_to_minutes` that takes a string representing the current time in the format HH:MM, where hours are in 24-hour format. The function should return the total time in minutes, considering both hours and minutes.
"""

def time_to_minutes(current_time):
    hours, minutes = map(int, current_time.split(':'))
    total_minutes = hours * 60 + minutes
    return total_minutes