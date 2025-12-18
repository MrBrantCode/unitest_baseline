"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given non-negative integer `n` using recursion, and handles large numbers correctly without causing a stack overflow.
"""

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer n using recursion.
    
    Args:
        n (int): A non-negative integer.
    
    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)