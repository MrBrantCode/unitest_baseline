"""
QUESTION:
Implement a function named `calculate_factorial` that calculates the factorial of a given non-negative integer `n`. The function should return the factorial of `n` if `n` is non-negative, and an error message if `n` is negative. The package that contains the `calculate_factorial` function should have a defined version number.
"""

def calculate_factorial(n):
    """
    Calculate the factorial of a given non-negative integer n.
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The factorial of n if n is non-negative, otherwise an error message.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result