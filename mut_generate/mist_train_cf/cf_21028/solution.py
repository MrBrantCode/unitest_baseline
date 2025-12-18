"""
QUESTION:
Write a function `get_number_of_days(month, year)` that calculates the total number of days in a given month and year, taking into account leap years. The month should be a valid integer between 1 and 12, and the year should be a valid integer greater than 0. The function should return the total number of days in the given month and year.
"""

def get_number_of_days(month, year):
    """
    Calculate the total number of days in a given month and year, taking into account leap years.

    Args:
    month (int): A valid integer between 1 and 12.
    year (int): A valid integer greater than 0.

    Returns:
    int: The total number of days in the given month and year.
    """

    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return 29
        else:
            return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30