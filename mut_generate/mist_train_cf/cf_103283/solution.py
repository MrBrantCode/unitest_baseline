"""
QUESTION:
Write a function named `days_in_month` that takes the year and month as input and returns the number of days in that month. The year and month are represented by integers, with the month being in the range 1-12. The function should handle leap years and different month lengths.
"""

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return 29
        else:
            return 28
    else:
        return 30