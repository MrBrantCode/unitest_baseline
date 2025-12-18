"""
QUESTION:
Write a function `max_sum` that takes a 2D array as input, calculates the sum of each row, and returns the maximum sum found.
"""

def max_sum(arr):
    """
    This function calculates the sum of each row in a 2D array and returns the maximum sum found.

    Args:
        arr (list): A 2D list of integers.

    Returns:
        int: The maximum sum of a row in the input array.
    """
    return max(sum(row) for row in arr)