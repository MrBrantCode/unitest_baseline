"""
QUESTION:
Write a function `factorial2(n)` that calculates the factorial of a given integer `n` and analyze its runtime complexity. The function should take an integer `n` as input and return its factorial.
"""

def factorial2(n):
    """
    Calculate the factorial of a given integer n.
    
    Args:
    n (int): The input integer.
    
    Returns:
    int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial2(n-1)