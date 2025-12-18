"""
QUESTION:
Write a function `get_days` that takes a month name and a year as input parameters and returns the number of days in that month for that specific year. The function should handle leap years and perform validation checks to ensure that the input month is a valid month name and the year is 1900 or later.
"""

import calendar

def get_days(month, year):
    # Validate year
    if year < 1900:
        return "Year must be 1900 or later."

    # Validate month
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    if month not in months:
        return "Invalid month."

    # Trivially calculate days in a month
    month_number = months.index(month) + 1  # Converts month name to month number
    days = calendar.monthrange(year, month_number)[1]  # Gets the number of days in the month

    return days