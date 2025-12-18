"""
QUESTION:
Write a function `check_range` that checks if a given number is within a specified range, inclusive, and has at most 3 decimal places. The function should return True if the number is within the range and has at most 3 decimal places, and False otherwise. The number and range boundaries can be decimals.
"""

def check_range(number, min_range, max_range):
    """
    Checks if a given number is within a specified range, inclusive, and has at most 3 decimal places.

    Args:
        number (float): The number to check.
        min_range (float): The lower boundary of the range.
        max_range (float): The upper boundary of the range.

    Returns:
        bool: True if the number is within the range and has at most 3 decimal places, False otherwise.
    """
    return min_range <= number <= max_range and round(number % 1, 3) == number % 1