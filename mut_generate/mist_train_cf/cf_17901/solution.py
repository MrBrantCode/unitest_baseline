"""
QUESTION:
Write a function called `sum_of_squares` that calculates the sum of the squares of the first n natural numbers using the formula n(n + 1)(2n + 1) / 6. The function should take one argument, `n`, which represents the number of terms, and return the calculated sum.
"""

def sum_of_squares(n):
    """
    Calculate the sum of the squares of the first n natural numbers.

    Args:
    n (int): The number of terms.

    Returns:
    int: The sum of the squares of the first n natural numbers.
    """
    return n * (n + 1) * (2 * n + 1) // 6