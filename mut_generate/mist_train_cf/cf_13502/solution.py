"""
QUESTION:
Create a function named `fibonacci` that calculates the n-th Fibonacci number using recursion. The function takes an integer `n` as input and returns the n-th Fibonacci number. The Fibonacci sequence is defined where a number is the sum of the two preceding ones, starting from 0 and 1. The input `n` is a positive integer.
"""

def fibonacci(n):
    """
    Calculate the n-th Fibonacci number using recursion.

    Args:
        n (int): A positive integer.

    Returns:
        int: The n-th Fibonacci number.
    """
    if n <= 0:
        return "Invalid input! n must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)