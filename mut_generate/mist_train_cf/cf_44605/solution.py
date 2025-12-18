"""
QUESTION:
Write a function `create_squares` that takes an integer `n` as input and returns a list of squares of all numbers from 0 to `n` (inclusive) that are even.
"""

def create_squares(n):
    """
    This function generates a list of squares of all numbers from 0 to n (inclusive) that are even.

    Args:
        n (int): The upper limit of the range of numbers to generate squares for.

    Returns:
        list: A list of squares of even numbers from 0 to n.
    """
    return [x**2 for x in range(n + 1) if x % 2 == 0]