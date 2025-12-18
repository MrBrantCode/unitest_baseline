"""
QUESTION:
Write a function called `gcd` that calculates the greatest common divisor (GCD) of two numbers using the Euclidean algorithm. The function should take two integers as input and return their GCD.
"""

def gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The GCD of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return a