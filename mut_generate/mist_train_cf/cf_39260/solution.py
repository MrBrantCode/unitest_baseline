"""
QUESTION:
Write a function `optimized_operation(N)` that calculates the sum of squares of numbers from 1 to `N`. The function should be optimized to run within a time limit of 0.2 seconds when called in a loop that increases `N` until the time limit is exceeded.
"""

def optimized_operation(N):
    """
    Calculate the sum of squares of numbers from 1 to N.

    Args:
        N (int): The upper limit of the range.

    Returns:
        int: The sum of squares of numbers from 1 to N.
    """
    return N * (N + 1) * (2 * N + 1) // 6