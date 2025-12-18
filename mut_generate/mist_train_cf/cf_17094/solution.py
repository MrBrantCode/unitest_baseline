"""
QUESTION:
Implement a function called `binary_exponentiation` that calculates the value of a number raised to a power without using any mathematical operators or built-in functions for exponentiation, with a time complexity of O(log n) or better. The function should take two integers as input: the base and the exponent, and return the result as an integer.
"""

def binary_exponentiation(base, exponent):
    """
    This function calculates the value of a number raised to a power without using any mathematical operators or built-in functions for exponentiation.
    
    Parameters:
    base (int): The base number.
    exponent (int): The exponent to which the base is raised.
    
    Returns:
    int: The result of the exponentiation.
    """
    
    # Initialize result to 1
    result = 1
    
    # Convert the exponent into its binary representation and iterate through each bit from right to left
    while exponent > 0:
        # If the bit is 1, multiply result by the base
        if exponent % 2 == 1:
            result *= base
        
        # Square the base
        base *= base
        
        # Right shift the exponent by 1 bit (divide by 2)
        exponent //= 2
    
    # After the iteration, result will contain the desired value
    return result