"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given non-negative integer `n` using recursion. The function should return `-1` if `n` is negative. What is the time complexity of this function?
"""

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer n using recursion.
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The factorial of n if n is non-negative, -1 otherwise.
    """
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)