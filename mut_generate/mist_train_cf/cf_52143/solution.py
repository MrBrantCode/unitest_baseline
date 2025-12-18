"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given number and use it to create a new list where each element is the factorial of the corresponding element in the input list. The function should work for non-negative integers and the input list will contain only non-negative integers.
"""

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer.

    Args:
    n (int): A non-negative integer.

    Returns:
    int: The factorial of n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)