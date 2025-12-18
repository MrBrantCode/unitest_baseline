"""
QUESTION:
Create a function named `total_days` that calculates the total number of days between two given dates in the format 'YYYY-MM-DD'. The function should validate the dates to ensure they are in the correct format and represent valid dates, considering leap years and proper day and month ranges. The function should also handle non-string inputs and return an error message if either date is invalid.
"""

from datetime import datetime

def total_days(date1_str, date2_str):
    try:
        date1 = datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.strptime(date2_str, '%Y-%m-%d')
        return abs((date2 - date1).days)
    except ValueError:
        return "Error: Invalid date format. Please provide in 'YYYY-MM-DD' format"