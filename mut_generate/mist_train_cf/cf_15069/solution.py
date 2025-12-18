"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a given positive integer `n`. The function should handle the base case where `n` is 0 or 1 and return the result of the recursive call for `n > 1`. Assume that `n` is a non-negative integer.
"""

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)