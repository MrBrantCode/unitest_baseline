"""
QUESTION:
Write a function `find_difference` that takes a list of numbers as input, sorts the list in ascending order, and returns the difference between the largest and smallest numbers in the list. The input list can be assumed to be non-empty.
"""

def find_difference(numbers):
    """
    This function calculates the difference between the largest and smallest numbers in a given list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The difference between the largest and smallest numbers in the list.
    """
    sorted_list = sorted(numbers)
    return sorted_list[-1] - sorted_list[0]