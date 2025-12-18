"""
QUESTION:
Implement a recursive function called "calculate_factorial" that takes an integer input 'x'. The function should return the factorial of 'x', defined as the product of all positive integers less than or equal to 'x'. If 'x' is a negative number, return an error message. The function should also handle the base case where 'x' is 0, returning 1, and should be able to handle large input values without causing a stack overflow error.
"""

def calculate_factorial(x):
    """
    Calculates the factorial of a given non-negative integer.

    Args:
    x (int): The input number.

    Returns:
    int: The factorial of the input number.
    str: An error message if the input number is negative.
    """
    if x < 0:
        return "Error: Factorials are only defined for non-negative integers."
    elif x == 0:
        return 1
    else:
        return x * calculate_factorial(x - 1)