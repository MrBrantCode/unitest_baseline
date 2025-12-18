"""
QUESTION:
Write a function called `days_between_dates` that takes two date strings in the format 'YYYY-MM-DD' as input and returns the number of days between these two dates, considering leap years. The function should handle dates where the years are the same and where the years are different.
"""

import calendar
from datetime import datetime

def days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.

    Args:
        date1 (str): The first date in the format 'YYYY-MM-DD'.
        date2 (str): The second date in the format 'YYYY-MM-DD'.

    Returns:
        int: The number of days between the two dates.
    """
    date1 = datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.strptime(date2, '%Y-%m-%d')
    
    return abs((date2 - date1).days)