"""
QUESTION:
Create a function called "factorial" that calculates the factorial of a given integer "n" using recursion. The function should have a time complexity of O(n) and a space complexity of O(n). Additionally, it should handle negative input numbers and return an error message "Error: Factorial is undefined for negative numbers."
"""

def factorial(n):
    """
    This function calculates the factorial of a given integer 'n' using recursion.
    
    Args:
    n (int): The input number for which the factorial needs to be calculated.
    
    Returns:
    int: The factorial of the input number if it is non-negative, otherwise an error message.
    """
    if n < 0:
        return "Error: Factorial is undefined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)