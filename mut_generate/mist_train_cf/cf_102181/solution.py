"""
QUESTION:
Write a function called `sum_of_cubes` that takes a positive integer as input and returns the sum of the cubes of all the digits in the number. The input number can have up to 10^18 digits.
"""

def sum_of_cubes(num):
    """
    Calculate the sum of the cubes of all the digits in a given number.

    Args:
        num (int): A positive integer.

    Returns:
        int: The sum of the cubes of all the digits in the number.
    """
    sum_of_cubes = 0
    while num > 0:
        digit = num % 10
        sum_of_cubes += digit ** 3
        num //= 10
    return sum_of_cubes