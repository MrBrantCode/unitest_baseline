"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given non-negative integer `n`. The function should use recursion and not include any loops. The input `n` is guaranteed to be a non-negative integer.
"""

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer n using recursion.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)