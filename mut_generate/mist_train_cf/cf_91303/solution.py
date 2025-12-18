"""
QUESTION:
Write a function named `is_leap_prime` that takes one argument, `year`, and returns `True` if the given year is both a leap year and a prime number, and `False` otherwise. A year is considered a leap year if it is evenly divisible by 4, except for end-of-century years which must be divisible by 400. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_leap_prime(year):
    """
    Checks if a given year is both a leap year and a prime number.

    Args:
    year (int): The year to check.

    Returns:
    bool: True if the year is both a leap year and a prime number, False otherwise.
    """

    # Check if the year is a leap year
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

    # Check if the year is a prime number
    if year < 2:
        is_prime = False
    else:
        for i in range(2, int(year/2) + 1):
            if year % i == 0:
                is_prime = False
                break
        else:
            is_prime = True

    # Return True if the year is both a leap year and a prime number, False otherwise
    return is_leap and is_prime