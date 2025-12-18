"""
QUESTION:
Write a function that uses a lambda expression and the reduce function to calculate the sum of all numbers in a list. The function should take a list of numbers as input and return the sum. The input list may contain any number of integers.
"""

from functools import reduce

def sum_numbers(numbers):
    """
    Calculate the sum of all numbers in a list using lambda expression and reduce function.

    Args:
    numbers (list): A list of integers.

    Returns:
    int: The sum of all numbers in the list.
    """
    return reduce(lambda x, y: x + y, numbers)