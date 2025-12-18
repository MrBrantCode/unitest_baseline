"""
QUESTION:
Create a function called `fibonacci(n)` that takes a positive integer `n` as input and returns the nth term of the Fibonacci sequence. The Fibonacci sequence starts with 0 as the 1st term and 1 as the 2nd term. The function should be implemented recursively. If `n` is not a positive integer, the function should return an error message.
"""

def fibonacci(n):
    """
    This function calculates the nth term of the Fibonacci sequence recursively.

    Args:
        n (int): A positive integer.

    Returns:
        int: The nth term of the Fibonacci sequence.
        str: An error message if n is not a positive integer.
    """
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)