"""
QUESTION:
Implement a function named `gcd` that calculates the greatest common divisor of two numbers. The function should take two positive integers `a` and `b` as input, where 1 <= a, b <= 10^9. The function should return the greatest common divisor (GCD) of `a` and `b` without using any built-in GCD functions or libraries.
"""

def gcd(a, b):
    """
    Calculate the greatest common divisor of two numbers.

    Args:
        a (int): The first positive integer.
        b (int): The second positive integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    # base case: if b is 0, then gcd(a, b) = a
    if b == 0:
        return a
    else:
        # recursively find the gcd of b and the remainder of a divided by b
        return gcd(b, a % b)