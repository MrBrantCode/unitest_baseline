"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given positive integer `n`, where 1 ≤ n ≤ 10. The function should return the product of all positive integers less than or equal to `n`.
"""

def factorial(n):
    """
    Calculate the factorial of a given positive integer n.

    Args:
        n (int): A positive integer between 1 and 10.

    Returns:
        int: The product of all positive integers less than or equal to n.
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)