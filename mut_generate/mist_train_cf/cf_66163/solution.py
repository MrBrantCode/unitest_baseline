"""
QUESTION:
Write a function named `computeSum` that takes a list of integers as input and returns the sum of even integers at odd indices in the list.
"""

def computeSum(lst):
    """
    This function calculates the sum of even integers at odd indices in the list.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The sum of even integers at odd indices.
    """
    return sum(num for idx, num in enumerate(lst) if idx % 2 != 0 and num % 2 == 0)