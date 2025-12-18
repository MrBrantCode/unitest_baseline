"""
QUESTION:
Design a function called `fib_checker` that takes an integer `num` as input and returns `True` if `num` is a Fibonacci number, and `False` otherwise. The function should efficiently handle values up to 100,000 and return an error message for non-positive inputs.
"""

def fib_checker(num):
    """
    Checks if a given number is a Fibonacci number.

    Args:
        num (int): The number to be checked.

    Returns:
        bool: True if num is a Fibonacci number, False otherwise.
        str: An error message if num is not a positive integer.
    """
    if num <= 0:
        return "Invalid input, number should be greater than 0"
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False