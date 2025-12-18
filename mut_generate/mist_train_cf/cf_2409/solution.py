"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given number `n` using tail recursion optimization. The function should accept an integer `n` that is greater than or equal to 1. If `n` is a floating-point number, it should be rounded down to the nearest integer. If `n` is a negative number, the function should return an error message.
"""

def factorial(n):
    """
    Calculate the factorial of a given number n using tail recursion optimization.

    Args:
        n (int or float): The input number. If float, it will be rounded down to the nearest integer.

    Returns:
        int: The factorial of n if n is a non-negative integer, otherwise an error message.
    """
    # Handle negative numbers
    if n < 0:
        return "Error: Input must be a positive integer"
    
    # Convert floating-point numbers to integers
    n = int(n)
    
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    # Helper function for tail recursion optimization
    def factorial_helper(n, accum):
        if n == 0:
            return accum
        return factorial_helper(n - 1, accum * n)
    
    return factorial_helper(n, 1)