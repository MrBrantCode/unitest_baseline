"""
QUESTION:
Write a function named `find_original_number` to calculate the original number given its quotient, divisor, and remainder when divided. The function should take three parameters: `quotient`, `divisor`, and `remainder`. Use the formula `quotient * divisor + remainder` to calculate the original number.
"""

def find_original_number(quotient, divisor, remainder):
    """
    Calculate the original number given its quotient, divisor, and remainder when divided.
    
    Parameters:
    quotient (int): The quotient of the division.
    divisor (int): The divisor of the division.
    remainder (int): The remainder of the division.
    
    Returns:
    int: The original number.
    """
    return quotient * divisor + remainder