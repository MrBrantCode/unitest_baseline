"""
QUESTION:
Write a function called calculate_arithmetic_mean that takes a list of integers as input and returns the arithmetic mean of the numbers in the list. The list will contain integers in the range 1-5.
"""

def calculate_arithmetic_mean(numbers):
    """
    This function calculates the arithmetic mean of a list of integers.

    Args:
        numbers (list): A list of integers.

    Returns:
        float: The arithmetic mean of the numbers in the list.
    """
    return sum(numbers) / len(numbers)