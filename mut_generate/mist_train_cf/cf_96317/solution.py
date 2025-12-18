"""
QUESTION:
Write a function `check_range` that takes in three parameters: a decimal number and a range defined by a minimum and maximum value (inclusive), and returns `True` if the number is within the range and has at most 3 decimal places, and `False` otherwise. The function should not modify the original number.
"""

def check_range(num, min_range, max_range):
    """
    Checks if a number is within a given range and has at most 3 decimal places.

    Args:
    num (float): The number to be checked.
    min_range (float): The minimum value of the range (inclusive).
    max_range (float): The maximum value of the range (inclusive).

    Returns:
    bool: True if the number is within the range and has at most 3 decimal places, False otherwise.
    """
    return min_range <= num <= max_range and round(num % 1, 3) == num % 1