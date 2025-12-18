"""
QUESTION:
Write a function `compute_time_difference` that takes two datetime objects as input and returns the difference in years, months, days, hours, and minutes. The function should be able to handle datetime objects with varying lengths of months and leap years.
"""

from dateutil.relativedelta import relativedelta
import datetime 

def compute_time_difference(DateTime1, DateTime2):
    """
    Compute the time difference between two datetime objects.

    Args:
    DateTime1 (datetime): The first datetime object.
    DateTime2 (datetime): The second datetime object.

    Returns:
    tuple: A tuple containing the difference in years, months, days, hours, and minutes.
    """
    delta = relativedelta(DateTime1, DateTime2)
    years = delta.years
    months = delta.months
    days = delta.days
    hours = delta.hours
    minutes = delta.minutes 
    return years, months, days, hours, minutes