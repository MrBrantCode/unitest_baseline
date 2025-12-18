"""
QUESTION:
Write a function `divide_numbers(x, y)` that takes two positive integers as input, performs integer division, and returns the quotient and remainder. Ensure the divisor is not zero and both numbers are positive integers; if not, return an error message.
"""

def divide_numbers(x, y):
    """
    This function performs integer division and returns the quotient and remainder.

    Args:
        x (int): The dividend (a positive integer).
        y (int): The divisor (a positive integer).

    Returns:
        tuple: A tuple containing the quotient and remainder, or an error message if input is invalid.
    """
    if x <= 0 or y <= 0:
        return "Error: Both numbers must be positive integers."
    
    if y == 0:
        return "Error: Division by zero is not allowed."
    
    quotient = x // y
    remainder = x % y
    
    return quotient, remainder