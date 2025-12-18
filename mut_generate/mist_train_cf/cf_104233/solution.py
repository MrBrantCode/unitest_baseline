"""
QUESTION:
Write a function called "factorial" that takes a non-negative integer as input and returns the factorial of that number. The function should be recursive and calculate the factorial as the product of all positive integers less than or equal to the input number.
"""

def factorial(n):
    """
    This function calculates the factorial of a given non-negative integer.
    
    Args:
        n (int): A non-negative integer.
    
    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)