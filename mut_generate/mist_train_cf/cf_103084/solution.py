"""
QUESTION:
Write a function named `get_number_of_days` that takes two integer parameters, `month` and `year`, and returns the number of days in the specified month. The function should correctly handle leap years for the month of February.
"""

def get_number_of_days(month, year):
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31