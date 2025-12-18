"""
QUESTION:
Write a function called `gcd` that takes two integers as input and returns their greatest common divisor. The function should not use any built-in gcd functions and should work with integers of up to 10^9 digits. The input integers can be positive or negative.
"""

def gcd(a, b):
    """
    Calculate the greatest common divisor of two integers using the Euclidean algorithm.
    
    Args:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a