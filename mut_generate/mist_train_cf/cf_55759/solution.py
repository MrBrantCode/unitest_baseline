"""
QUESTION:
Write a function named `check_days` that takes two parameters, `month` and `year`, where `month` is an integer between 1 and 12 representing a month of the year, and `year` is an integer representing the year. The function should return `True` if the month has exactly 30 days and `False` otherwise. It should also handle February correctly by considering leap years.
"""

def check_days(month, year):
    thirty_days_months = [4, 6, 9, 11]
    if month in thirty_days_months:
        return True
    elif month == 2:
        return False
    else:
        return False