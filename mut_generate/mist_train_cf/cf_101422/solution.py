"""
QUESTION:
Calculate the exact duration in days between two given dates, inclusive, considering leap years and daylight saving time adjustments. 

Write a function `calculate_duration` that takes two parameters: `start_date` (January 1st) and `end_date` (April 5th), and returns the total number of days between the two dates. The function should account for leap years and daylight saving time adjustments, but assume no time zone changes occurred during this period.
"""

import datetime

def calculate_duration(start_date, end_date):
    """
    Calculate the exact duration in days between two given dates, inclusive, 
    considering leap years and daylight saving time adjustments.

    Args:
        start_date (datetime.date): The start date.
        end_date (datetime.date): The end date.

    Returns:
        int: The total number of days between the two dates.
    """
    days = (end_date - start_date).days + 1
    for year in range(start_date.year, end_date.year+1):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days += 1
    if start_date <= datetime.date(2021, 3, 14) and end_date >= datetime.date(2021, 3, 14):
        days -= 1
    return days