"""
QUESTION:
Write a function `factorial(n)` to calculate the factorial of a given number `n` using recursion. The function should be called and its result printed when the given number `n` is divisible by both 3 and 5.
"""

def factorial(n):
    """
    Calculate the factorial of a given number n using recursion.
    
    Args:
        n (int): The number to calculate the factorial for.
    
    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)