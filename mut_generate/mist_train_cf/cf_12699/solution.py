"""
QUESTION:
Write a function `factorial` that takes a positive integer `n` (where 1 ≤ n ≤ 10) as input and returns its factorial, which is the product of all positive integers less than or equal to `n`.
"""

def factorial(n):
    """
    Calculate the factorial of a positive integer n.

    Args:
        n (int): A positive integer where 1 ≤ n ≤ 10.

    Returns:
        int: The factorial of n.
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)