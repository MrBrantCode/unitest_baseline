"""
QUESTION:
Write a function `f(n)` that calculates the sum of all numbers from 1 to n using recursion. The function should take an integer `n` as input and return the sum of integers from 1 to `n`. The function should not use any loops or built-in sum functions.
"""

def f(n):
    """
    This function calculates the sum of all numbers from 1 to n using recursion.

    Args:
    n (int): The upper limit of the range of numbers to be summed.

    Returns:
    int: The sum of integers from 1 to n.
    """
    if n <= 1:
        return n
    else:
        return n + f(n - 1)