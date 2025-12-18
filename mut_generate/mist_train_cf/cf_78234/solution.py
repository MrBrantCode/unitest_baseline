"""
QUESTION:
Write a function named `sort_decimals` that takes a list of decimal numbers as input, and returns the list sorted in descending order.
"""

def sort_decimals(decimal_numbers):
    """
    Sorts a list of decimal numbers in descending order.

    Args:
        decimal_numbers (list): A list of decimal numbers.

    Returns:
        list: The sorted list in descending order.
    """
    return sorted(decimal_numbers, reverse=True)