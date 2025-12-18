"""
QUESTION:
Create a function `is_leap_year(year)` that determines whether a given year is a leap year using recursion and only logical operators, without using any mathematical functions or operators except modulus, which is allowed for this problem. The function should return a boolean value indicating whether the year is a leap year or not.
"""

def entrance(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False