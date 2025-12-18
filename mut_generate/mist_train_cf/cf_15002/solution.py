"""
QUESTION:
Create a function called `gcd` to calculate the greatest common divisor of two integers using the Euclidean algorithm. The function should take two integers as input and return their greatest common divisor.
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
    while b:
        a, b = b, a % b
    return a