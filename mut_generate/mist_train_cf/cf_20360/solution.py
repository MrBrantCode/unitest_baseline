"""
QUESTION:
Write a function named `fibonacci(n)` that takes a single integer `n` as input and returns the nth Fibonacci number using a recursive approach without memoization. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting with 0 and 1. The input `n` is restricted to the range 0 <= n <= 30.
"""

def fibonacci(n):
    """
    Returns the nth Fibonacci number using a recursive approach without memoization.

    Args:
    n (int): The position of the Fibonacci number to be calculated (0 <= n <= 30).

    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)