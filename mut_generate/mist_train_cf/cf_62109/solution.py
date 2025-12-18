"""
QUESTION:
Write a function `calculate_interval` that takes a list of numbers as input and returns the difference between the maximum and minimum elements in the list. The input list is guaranteed to be non-empty.
"""

def calculate_interval(numbers):
    """
    This function calculates the difference between the maximum and minimum elements in a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The difference between the maximum and minimum elements in the list.
    """
    return max(numbers) - min(numbers)