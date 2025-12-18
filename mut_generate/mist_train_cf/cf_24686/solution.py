"""
QUESTION:
Write a function `date_difference_in_days` that calculates the difference between two given dates in days. The input dates will be provided as strings in the format "YYYY-MM-DD". The function should return the absolute difference in days between the two dates.
"""

from datetime import datetime

def date_difference_in_days(date1, date2):
    """
    Calculate the absolute difference in days between two dates.

    Args:
        date1 (str): The first date in "YYYY-MM-DD" format.
        date2 (str): The second date in "YYYY-MM-DD" format.

    Returns:
        int: The absolute difference in days between the two dates.
    """
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")
    difference = abs((date2 - date1).days)
    return difference