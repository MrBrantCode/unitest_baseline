"""
QUESTION:
Implement a recursive function `gcd(a, b)` that calculates the Greatest Common Divisor of two integers `a` and `b` without using built-in functions or libraries. The function should take two integers as input and return their GCD.
"""

def gcd(a, b):
    """
    Calculate the Greatest Common Divisor of two integers a and b.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The Greatest Common Divisor of a and b.
    """
    if b == 0:
        return a
    else:
        remainder = a % b
        return gcd(b, remainder)