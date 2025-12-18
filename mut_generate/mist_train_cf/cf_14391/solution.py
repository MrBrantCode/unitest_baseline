"""
QUESTION:
Implement a function `gcd` that calculates the greatest common divisor of two numbers using the Euclidean algorithm. The function should take two integers as input and return their greatest common divisor.
"""

def gcd(a, b):
    """
    Calculate the greatest common divisor of two numbers using the Euclidean algorithm.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a