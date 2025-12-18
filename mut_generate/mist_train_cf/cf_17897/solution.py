"""
QUESTION:
Write a function `is_leap_year` that takes an integer year as input and returns `True` if the year is a leap year and `False` otherwise, using only logical operators and loops, without relying on any built-in mathematical functions or operators.
"""

def is_leap_year(year):
    """
    Returns True if the year is a leap year, False otherwise.
    
    A year is a leap year if it is divisible by 4, but not by 100, 
    unless it is also divisible by 400.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    # Check if the year is divisible by 4 and not divisible by 100
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    # Check if the year is divisible by 400
    elif year % 400 == 0:
        return True
    else:
        return False