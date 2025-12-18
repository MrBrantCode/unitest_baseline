"""
QUESTION:
Write a function `calculate_average` that takes a list of numbers as input and returns the average of these numbers without using any arithmetic operations for the calculation of the average itself.
"""

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers without using arithmetic operations.

    Args:
    numbers (list): A list of numbers.

    Returns:
    float: The average of the numbers.
    """
    sum_of_numbers = sum(numbers)
    count_of_numbers = len(numbers)
    return sum_of_numbers / count_of_numbers