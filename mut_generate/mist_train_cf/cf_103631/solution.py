"""
QUESTION:
Write a recursive function `fib` that takes an integer `n` as input and returns the nth Fibonacci number, where the Fibonacci sequence is defined as the first two numbers being 0 and 1, and each subsequent number being the sum of the two preceding ones. The function should raise an exception if `n` is not a non-negative integer.
"""

def fib(n):
    """
    Returns the nth Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to return.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        Exception: If n is not a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise Exception("n must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)