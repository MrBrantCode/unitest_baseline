"""
QUESTION:
Write a recursive function called `fibonacci(n)` that calculates the nth Fibonacci number for a given positive integer `n`. The function should have a time complexity of O(2^n) and follow these conditions: if `n` is less than or equal to 0, return 0; if `n` is 1, return 1; otherwise, return the sum of the results from the function called with `n-1` and `n-2` as arguments.
"""

def fibonacci(n):
    """
    This function calculates the nth Fibonacci number for a given positive integer n.

    Args:
        n (int): A positive integer.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)