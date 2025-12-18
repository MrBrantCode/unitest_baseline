"""
QUESTION:
Write a function `fib` that calculates the nth Fibonacci number using recursion. The Fibonacci sequence is defined where each number is the sum of the two preceding ones, starting from 0 and 1. Implement this function with the base case where `n` is 0 or 1, and return the corresponding Fibonacci number. The function should only accept non-negative integers.
"""

def fib(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Args:
    n (int): The index of the Fibonacci number to calculate.

    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)