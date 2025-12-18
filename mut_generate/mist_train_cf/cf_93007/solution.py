"""
QUESTION:
Design a function named `is_leap_year` that takes an integer year as input and returns a boolean indicating whether the year is a leap year on the Gregorian calendar. The function should follow these rules: a year is a leap year if it is divisible by 4 but not by 100 unless it is also divisible by 400, and the Gregorian calendar is used for years 1582 and later, excluding years that are divisible by 100 but not by 400.
"""

def is_leap_year(year):
    if year < 1582:
        if year % 4 == 0:
            return True
        else:
            return False
    else:
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True