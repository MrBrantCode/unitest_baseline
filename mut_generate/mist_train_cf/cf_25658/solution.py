"""
QUESTION:
Write a function named `factorial(num)` that calculates the factorial of a given integer `num`. The function should recursively calculate the factorial and return the result. The input `num` should be a non-negative integer.
"""

def factorial(num):
    """
    Calculates the factorial of a given non-negative integer.

    Args:
    num (int): A non-negative integer.

    Returns:
    int: The factorial of the given number.
    """
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)