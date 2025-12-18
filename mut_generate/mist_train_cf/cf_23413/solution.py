"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given integer `n` using a non-recursive algorithm. The function should return the factorial of `n`. Assume that `n` is a non-negative integer.
"""

def factorial(n): 
    """
    Calculate the factorial of a given non-negative integer n using a non-recursive algorithm.

    Args:
    n (int): A non-negative integer.

    Returns:
    int: The factorial of n.
    """
    res = 1 
    for i in range(2,n+1): 
        res = res * i 
    return res 