"""
QUESTION:
Write a function `hours_since_1970` that calculates the total number of hours from January 1st, 1970, until a given date. The function should take a date as input and return the total number of hours as an integer.
"""

from datetime import datetime

def hours_since_1970(date):
    """
    Calculate the total number of hours from January 1st, 1970, until a given date.

    Args:
        date (datetime): The date until which the hours are calculated.

    Returns:
        int: The total number of hours since January 1st, 1970.
    """
    # Set the start date to January 1st, 1970
    start_date = datetime(1970, 1, 1)

    # Calculate the difference between the given date and the start date
    time_diff = date - start_date

    # Calculate the total number of hours
    total_hours = time_diff.days * 24 + time_diff.seconds // 3600

    return total_hours