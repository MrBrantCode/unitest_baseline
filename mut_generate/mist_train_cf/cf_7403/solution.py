"""
QUESTION:
Write a function named `validate_dates` that takes a list of two strings representing dates in the format "yyyy-mm-dd" and returns a boolean indicating whether the dates are valid. The dates are valid if they are in increasing order, within the range of years 2000-2025, and fall on weekdays (Monday to Friday). The function should consider the Gregorian calendar system, including leap years and the correct number of days in each month.
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