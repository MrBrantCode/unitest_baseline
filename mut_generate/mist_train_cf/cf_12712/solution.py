"""
QUESTION:
Write a function named `six_months_later` that takes an integer representing a month of the year (1-12) and returns the name of the month that is 6 months later, considering a wrap-around to the beginning of the year if necessary.
"""

import datetime

def six_months_later(month):
    """
    Returns the name of the month that is 6 months later than the given month.

    Args:
        month (int): The month of the year (1-12)

    Returns:
        str: The name of the month 6 months later
    """
    month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    future_month = (month + 5) % 12 + 1
    return month_names[future_month - 1]