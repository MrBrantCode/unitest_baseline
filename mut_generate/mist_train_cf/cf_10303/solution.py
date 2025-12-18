"""
QUESTION:
Write a function `is_leap_prime_year` that takes an integer `year` as input and returns `True` if the year is both a leap year and a prime number, and `False` otherwise. The function should handle any integer input.
"""

def is_leap_prime_year(year):
    """
    Checks if a given year is both a leap year and a prime number.

    Args:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is both a leap year and a prime number, False otherwise.
    """

    # Check if year is a leap year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap = True
            else:
                is_leap = False
        else:
            is_leap = True
    else:
        is_leap = False

    # Check if year is a prime number
    if year < 2:
        is_prime = False
    else:
        for i in range(2, int(year/2) + 1):
            if year % i == 0:
                is_prime = False
                break
        else:
            is_prime = True

    # Return True if year is both leap and prime
    return is_leap and is_prime