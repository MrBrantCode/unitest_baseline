"""
QUESTION:
Design a function `is_leap_year` that determines if a given year is a leap year. A leap year is exactly divisible by 4, except for end-of-century years which must be divisible by 400. This means that in the year 2000 was a leap year, although 1900 was not. The function should also consider the Gregorian calendar, which was introduced in 1582, and the proleptic Gregorian calendar used by the International Organization for Standardization (ISO). The function should return True if the year is a leap year and False otherwise.
"""

def is_leap_year(year):
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