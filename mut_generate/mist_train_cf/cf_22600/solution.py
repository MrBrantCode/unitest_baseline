"""
QUESTION:
Create a function named `sort_and_stringify` that takes a list of integers as input. The function should return a string of the input numbers in ascending order, separated by commas. The length of the input list should be at least 5. The input list may contain negative numbers.
"""

def sort_and_stringify(numbers):
    """
    This function takes a list of integers, sorts them in ascending order, 
    and returns a string of the numbers separated by commas.

    Args:
        numbers (list): A list of integers with a minimum length of 5.

    Returns:
        str: A string of the input numbers in ascending order, separated by commas.
    """
    return ",".join(map(str, sorted(numbers)))