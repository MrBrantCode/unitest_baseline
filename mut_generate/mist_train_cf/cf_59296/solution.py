"""
QUESTION:
Create a function named `find_remainder` that takes two integers `dividend` and `divisor` as parameters and returns the remainder of `dividend` divided by `divisor` without using the modulus operator. The function should use the mathematical definition of the remainder, where the remainder is the integer leftover after division.
"""

def find_remainder(dividend, divisor):
    """
    This function calculates the remainder of dividend divided by divisor without using the modulus operator.
    
    Parameters:
    dividend (int): The number being divided.
    divisor (int): The number by which we are dividing.
    
    Returns:
    int: The remainder of the division.
    """
    # The quotient is the integer part of the division
    quotient = dividend // divisor
    # The remainder is what remains after subtracting divisor*quotient from the dividend
    remainder = dividend - quotient * divisor
    return remainder