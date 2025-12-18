"""
QUESTION:
Write a function `get_num_days(year, month)` that takes an integer `year` and a string `month` as input, and returns the number of days in the given `month` and `year`, taking into account leap years. The `month` input should be a full month name (e.g., "January", "February", etc.).
"""

def get_num_days(year, month):
    days_in_month = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) and month == "February":
        return 29
    else:
        return days_in_month[month]