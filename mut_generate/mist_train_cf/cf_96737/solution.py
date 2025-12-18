"""
QUESTION:
Design a function `is_leap_year(year)` that checks if a given year is a leap year according to the Gregorian calendar, taking into account the exceptions introduced by the Julian calendar reform in 1582. The function should return `True` if the year is a leap year and `False` otherwise. The function must correctly handle years before 1582, the year 1582 itself, and years after 1582 that are divisible by 100 but not by 400.
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