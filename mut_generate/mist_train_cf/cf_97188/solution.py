"""
QUESTION:
Implement a function named `factorial` that calculates the factorial of a given integer `n`. The function should return an error message if `n` is a negative number. The function should have a time complexity of O(n).
"""

def factorial(n):
    """
    This function calculates the factorial of a given integer n.
    
    Args:
        n (int): The input number for which the factorial is calculated.
    
    Returns:
        int or str: The factorial of n if n is non-negative, otherwise an error message.
    """
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)