"""
QUESTION:
Write a function called `factorial(n)` that takes a non-negative integer `n` as input and returns the factorial of `n`. The function should use recursion to calculate the factorial, and you should determine and state the big-O time complexity of the algorithm. The input `n` is guaranteed to be a non-negative integer.
"""

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)