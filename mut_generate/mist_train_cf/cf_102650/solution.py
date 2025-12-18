"""
QUESTION:
Create a function named `time_to_minutes` that takes a string representing time in the format HH:MM, where hours are in 24-hour format. Return the total time in minutes. The function should assume the input string will always be in the correct format, with both hours and minutes separated by a colon.
"""

def time_to_minutes(current_time):
    hours, minutes = map(int, current_time.split(':'))
    total_minutes = hours * 60 + minutes
    return total_minutes