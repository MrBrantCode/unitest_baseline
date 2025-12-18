"""
QUESTION:
Write a function `count_first_sundays(year)` that calculates the number of Sundays in a given year that fall on the first of a month, taking into account leap years. The function should return the count of such Sundays. The input year is constrained between 1900 and 2100 (inclusive).
"""

import calendar

def count_first_sundays(year):
    count = 0
    for month in range(1, 13):
        # Check if the first day of the month is a Sunday
        if calendar.weekday(year, month, 1) == 6:
            count += 1
    return count