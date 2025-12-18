"""
QUESTION:
Write a function `validate_dates` that takes a list of two date strings in the format "yyyy-mm-dd" as input. The function should return `True` if the dates are in increasing order, are between the years 2000 and 2025 (inclusive), and fall on weekdays (Monday to Friday) only, and `False` otherwise.
"""

import datetime

def validate_dates(dates):
    start_date = datetime.datetime.strptime(dates[0], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(dates[1], "%Y-%m-%d")

    # Check if dates are in increasing order
    if start_date >= end_date:
        return False

    # Check if dates are within the range 2000-2025
    if start_date.year < 2000 or end_date.year > 2025:
        return False

    # Check if dates fall on weekdays only
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() >= 5:  # Saturday or Sunday
            return False
        current_date += datetime.timedelta(days=1)

    return True