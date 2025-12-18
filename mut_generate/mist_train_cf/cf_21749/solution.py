"""
QUESTION:
Design a function `is_leap_year(year)` that determines if a given year is a leap year and falls on the Gregorian calendar, taking into account the exceptions to the Gregorian calendar introduced by the Julian calendar reform in 1582. The function should return `True` if the year is a leap year on the Gregorian calendar and `False` otherwise.
"""

def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 != 0:
        return False
    # Check if the year is divisible by 100 but not by 400
    elif year % 100 == 0 and year % 400 != 0:
        return False
    # Check if the year falls on the Gregorian calendar
    elif year < 1582:
        return False
    # Check if the year falls within the Julian calendar reform in 1582
    elif year == 1582:
        return False
    elif year > 1582 and year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True