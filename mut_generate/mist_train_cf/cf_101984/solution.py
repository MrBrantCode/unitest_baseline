"""
QUESTION:
Write a function named sum_of_squares that takes a list of integers as input and returns the sum of the squares of these integers that are divisible by 3 but not by both 2 and 5.
"""

def sum_of_squares(numbers):
    """
    This function calculates the sum of the squares of integers in a list that are divisible by 3 but not by both 2 and 5.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of the squares of integers that meet the specified conditions.
    """
    return sum(i**2 for i in numbers if i % 3 == 0 and not (i % 2 == 0 and i % 5 == 0))