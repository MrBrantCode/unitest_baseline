"""
QUESTION:
Write a function named `gcd_euclidean` to calculate the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm. The function should take two integers as input and return their GCD.
"""

def gcd_euclidean(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.

    Args:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The GCD of a and b.
    """
    while b:
        a, b = b, a % b
    return a