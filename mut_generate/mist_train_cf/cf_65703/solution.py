"""
QUESTION:
Write a function `find_gcd4(x1, x2, x3, x4)` that takes four integer inputs and returns their Greatest Common Divisor (GCD), also known as the Highest Common Factor (HCF), by utilizing the built-in `math.gcd()` function.
"""

import math

def find_gcd4(x1, x2, x3, x4):
    """
    Calculate the Greatest Common Divisor (GCD) of four integers.
    
    Parameters:
    x1 (int): The first integer.
    x2 (int): The second integer.
    x3 (int): The third integer.
    x4 (int): The fourth integer.
    
    Returns:
    int: The GCD of the four integers.
    """
    temp = math.gcd(x1, x2)
    temp = math.gcd(temp, x3)
    result = math.gcd(temp, x4)

    return result