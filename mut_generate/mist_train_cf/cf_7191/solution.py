"""
QUESTION:
Design a function named `is_leap_year_gregorian` that determines if a given year is a leap year and falls on the Gregorian calendar. The function should consider the exceptions introduced by the Julian calendar reform in 1582. The function should return True if the year is a leap year on the Gregorian calendar and False otherwise. The input is a single integer year. The function should handle years before 1582 and apply the leap year rules of the Gregorian calendar, where a year is a leap year if it is divisible by 4, except for years that are divisible by 100 but not by 400.
"""

def is_leap_year_gregorian(year):
    # Check if the year is valid according to the Gregorian calendar
    if year < 1582:
        return False

    # Check if the year is divisible by 4
    if year % 4 != 0:
        return False

    # Check if the year is divisible by 100
    if year % 100 == 0:
        # Check if the year is divisible by 400
        if year % 400 == 0:
            return True
        else:
            return False

    # The year is divisible by 4 but not by 100
    return True