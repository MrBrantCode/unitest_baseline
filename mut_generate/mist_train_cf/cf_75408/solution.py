"""
QUESTION:
Design a recursive function called `fibonacci(n)` to calculate the nth Fibonacci number. The function should return the correct Fibonacci number for the given input `n`, where `n` is a positive integer. If `n` is less than or equal to 0, the function should return an error message.
"""

def fibonacci(n):
    """
    This function calculates the nth Fibonacci number using recursion.

    Args:
        n (int): The position of the Fibonacci number to be calculated.

    Returns:
        int: The nth Fibonacci number if n is a positive integer, otherwise an error message.
    """
    if n <= 0:
        return "Input should be greater than 0."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)