"""
QUESTION:
Create a function `perfect_squares` that takes a list of integers as input and returns a new list containing only the perfect squares from the input list. A perfect square is a number that can be expressed as the square of an integer. Use a list comprehension to solve this problem.
"""

from math import sqrt

def perfect_squares(numbers):
    """
    Returns a new list containing only the perfect squares from the input list.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list of perfect squares.
    """
    return [number for number in numbers if sqrt(number).is_integer()]