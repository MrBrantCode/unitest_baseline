"""
QUESTION:
Write a function named `solutions` that takes a non-empty list of integers as input and returns the sum of the odd elements found at even-indexed positions within the list.
"""

def solutions(lst):
    """
    This function calculates the sum of odd elements found at even-indexed positions within a given list.

    Args:
        lst (list): A non-empty list of integers.

    Returns:
        int: The sum of the odd elements found at even-indexed positions.
    """
    return sum(num for idx, num in enumerate(lst) if idx % 2 == 0 and num % 2 != 0)