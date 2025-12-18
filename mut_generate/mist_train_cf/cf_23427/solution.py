"""
QUESTION:
Create a function named `fib` to calculate the sum of the first `n` Fibonacci numbers. The `fib` function should take an integer `n` as input and return the `n`-th Fibonacci number. Use the `fib` function to calculate the sum of the Fibonacci numbers.
"""

def fib(n):
    """
    Calculate the nth Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)