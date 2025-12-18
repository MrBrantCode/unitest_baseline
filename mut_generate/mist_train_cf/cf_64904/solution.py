"""
QUESTION:
Write a function named `fibonacci` that takes a single integer `n` as input and returns the nth Fibonacci number. Do not worry about the efficiency of the function. 

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def fibonacci(n):
    """
    Returns the nth Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to return.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)