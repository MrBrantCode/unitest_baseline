"""
QUESTION:
Write a function called `check_sum_of_squares(n)` that takes an integer `n` as input and returns a boolean indicating whether `n` can be represented as the sum of two perfect squares. Use this function to find all numbers in a given list that can be represented in this way.
"""

def check_sum_of_squares(n):
    """
    Checks if a number can be represented as the sum of two perfect squares.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number can be represented as the sum of two perfect squares, False otherwise.
    """
    for i in range(0, int(n ** 0.5) + 1):
        for j in range(i, int(n ** 0.5) + 1):
            if i * i + j * j == n:
                return True
    return False