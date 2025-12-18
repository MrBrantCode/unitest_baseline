"""
QUESTION:
Create a function named `convert_milliseconds_to_hours` that takes an integer representing milliseconds as input and returns the equivalent hours as a floating point number. The function should use the conversion factor that 1 hour is equal to 3,600,000 milliseconds.
"""

def convert_milliseconds_to_hours(milliseconds):
    # 1 hour is equal to 3.6e+6 milliseconds
    hours = milliseconds / 3.6e+6
    return hours