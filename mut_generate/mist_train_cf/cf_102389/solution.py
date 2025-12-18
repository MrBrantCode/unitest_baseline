"""
QUESTION:
Write a function `check_number_in_range` that takes in three parameters: `number`, `min_range`, and `max_range`, all of which are decimal numbers. The function should check if `number` is within the inclusive range of `min_range` and `max_range`, if `number` is positive, and if `number` has at most 3 decimal places.
"""

def check_number_in_range(number, min_range, max_range):
    """
    Checks if a number is within a given inclusive range, is positive, and has at most 3 decimal places.

    Args:
        number (float): The number to be checked.
        min_range (float): The minimum value of the range (inclusive).
        max_range (float): The maximum value of the range (inclusive).

    Returns:
        bool: True if the number meets the conditions, False otherwise.
    """
    return min_range <= number <= max_range and number >= 0 and round(number, 3) == number