"""
QUESTION:
Design a function named `is_leap_year` that checks if a given year is a leap year and falls on the Gregorian calendar. The function should take an integer year as input and return True if the year is a leap year on the Gregorian calendar, False otherwise. The function should consider the following rules: 
- A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.
- A year falls on the Gregorian calendar if it is 1582 or later, and years divisible by 100 are only leap years if they are also divisible by 400.
"""

def is_leap_year(year):
    return year >= 1582 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)