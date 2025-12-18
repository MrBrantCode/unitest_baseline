"""
QUESTION:
Write a function named `factorial(n)` that takes a non-negative integer `n` as input and returns its factorial. The function must handle the base case where `n` equals 0, and it should either use recursive or iterative methods to compute the factorial.
"""

def factorial(n):
    """
    This function calculates the factorial of a given non-negative integer n.

    Args:
    n (int): A non-negative integer.

    Returns:
    int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)