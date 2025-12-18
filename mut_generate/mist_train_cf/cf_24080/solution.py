"""
QUESTION:
Create a function `next_fibonacci` to calculate the next Fibonacci number from a given number. The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, starting with 0 and 1. The function should take a single argument, the current number, and return the next number in the sequence. The input number is assumed to be a non-negative integer.
"""

def next_fibonacci(n):
    """
    Calculate the next Fibonacci number from a given number.

    Args:
        n (int): The current number in the Fibonacci sequence.

    Returns:
        int: The next number in the Fibonacci sequence.
    """
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return a + b