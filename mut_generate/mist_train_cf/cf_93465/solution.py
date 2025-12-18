"""
QUESTION:
Write a function `calculate_seconds(hours, minutes)` that calculates the total number of seconds in a given number of hours and minutes. The function should take two parameters: `hours` and `minutes`, and return the total number of seconds. There are 60 seconds in a minute and 60 minutes in an hour.
"""

def calculate_seconds(hours, minutes):
    total_minutes = hours * 60 + minutes
    total_seconds = total_minutes * 60
    return total_seconds