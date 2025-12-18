"""
QUESTION:
Compute the greatest common divisor (GCD) of two given integers without using any built-in GCD functions. Create a function named `gcd` that takes two integers `a` and `b` as input and returns their GCD. Assume that both `a` and `b` are non-negative integers.
"""

def gcd(a, b):
    """
    Compute the greatest common divisor (GCD) of two given integers.

    Args:
    a (int): The first non-negative integer.
    b (int): The second non-negative integer.

    Returns:
    int: The greatest common divisor of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return a