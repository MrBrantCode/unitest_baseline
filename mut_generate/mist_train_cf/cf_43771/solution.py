"""
QUESTION:
Write a function `is_leap` that takes an integer year as input and returns `True` if the year is a leap year according to the Gregorian calendar rules, and `False` otherwise. Then, use this function to calculate the total number of leap years from 1582 to the current year and predict the next 10 leap years. The function should not take any arguments other than the year to check. The Gregorian calendar rules are as follows: a year is a leap year if it is divisible by 4, except for end-of-century years which must be divisible by 400.
"""

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False