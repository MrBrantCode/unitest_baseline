"""
QUESTION:
Find the sum of the squares of the first N natural numbers for a given large positive integer N (N >= 10^6). Implement a function named `sum_of_squares` that takes an integer N as input and returns the sum of the squares of the first N natural numbers.
"""

def sum_of_squares(N):
    """
    Calculate the sum of the squares of the first N natural numbers.

    Args:
        N (int): A positive integer.

    Returns:
        int: The sum of the squares of the first N natural numbers.
    """
    return N * (N + 1) * (2 * N + 1) // 6