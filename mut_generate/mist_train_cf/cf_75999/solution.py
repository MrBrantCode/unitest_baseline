"""
QUESTION:
Design a function named `convert_milliseconds_to_hours` that takes one argument `milliseconds` and returns the equivalent duration in hours. The function should accurately handle decimal precision, rounding the result to a specified number of decimal places.
"""

def convert_milliseconds_to_hours(milliseconds):
    """
    Converts milliseconds to hours.

    Args:
    milliseconds (int): Time in milliseconds.

    Returns:
    float: Time in hours rounded to 3 decimal places.
    """
    hours = milliseconds / 3600000
    rounded_hours = round(hours, 3)
    return rounded_hours