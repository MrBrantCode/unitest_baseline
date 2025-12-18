"""
QUESTION:
Write a function `fibonacci(n)` that calculates the nth Fibonacci number using a recursive algorithm without using any additional variables or data structures. The function should take an integer `n` as input and return the corresponding Fibonacci number.
"""

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using a recursive algorithm.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)