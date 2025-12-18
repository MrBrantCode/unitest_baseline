"""
QUESTION:
Write a function `seconds_in_year` that takes an integer representing a year as input and returns the number of seconds in that year, considering leap years. The function should determine whether the input year is a leap year and return the correct total number of seconds accordingly.
"""

def seconds_in_year(year):
    """
    Calculate the number of seconds in a year, considering leap years.

    Args:
        year (int): The input year.

    Returns:
        int: The total number of seconds in the given year.
    """
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        # Leap year
        return 366 * 24 * 60 * 60
    else:
        # Non-leap year
        return 365 * 24 * 60 * 60