"""
QUESTION:
Calculate the factorial for each integer from 1 up to a provided number, limiting the calculation to the first 20 factorials. Write a function named `factorial` that takes an integer `n` as input and returns its factorial. The function should not use the math.factorial function from Python's math module.
"""

def factorial(n):
    """
    Calculate the factorial of a given integer.

    Args:
        n (int): The input number.

    Returns:
        int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)