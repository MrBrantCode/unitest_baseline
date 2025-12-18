"""
QUESTION:
Write a function `calculate_week_difference` that takes two date strings in the format "YYYY-MM-DD" as input and returns the absolute difference between the two dates in weeks.
"""

from datetime import datetime

def calculate_week_difference(date1, date2):
    """
    Calculate the absolute difference between two dates in weeks.

    Args:
        date1 (str): The first date in the format "YYYY-MM-DD".
        date2 (str): The second date in the format "YYYY-MM-DD".

    Returns:
        int: The absolute difference between the two dates in weeks.
    """
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")

    difference = abs((date2 - date1).days)
    weeks = difference // 7

    return weeks