"""
QUESTION:
Write a function to calculate the sum of the first n positive integers. The function should be optimized to handle large values of n efficiently. The function name should be `sum_of_integers`.
"""

def sum_of_integers(n):
    """
    Calculate the sum of the first n positive integers.

    Args:
        n (int): The number of positive integers to sum.

    Returns:
        int: The sum of the first n positive integers.
    """
    return (n * (n + 1)) // 2