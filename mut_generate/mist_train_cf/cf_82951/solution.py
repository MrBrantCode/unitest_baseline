"""
QUESTION:
Write a function named `date_discrepancy` to calculate the total number of days between two given dates. The function should take two string arguments `date1` and `date2` in the format "YYYY-MM-DD". The function should return an integer representing the absolute difference in days between the two dates.
"""

from datetime import datetime

def date_discrepancy(date1, date2):
    """
    Calculate the total number of days between two given dates.

    Args:
        date1 (str): The first date in the format "YYYY-MM-DD".
        date2 (str): The second date in the format "YYYY-MM-DD".

    Returns:
        int: The absolute difference in days between the two dates.
    """
    date_format = "%Y-%m-%d"
    date1_obj = datetime.strptime(date1, date_format)
    date2_obj = datetime.strptime(date2, date_format)
    discrepancy = abs((date2_obj - date1_obj).days)
    return discrepancy