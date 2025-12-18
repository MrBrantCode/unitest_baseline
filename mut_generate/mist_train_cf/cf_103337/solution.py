"""
QUESTION:
Implement a function named `gcd` that calculates the greatest common divisor (GCD) of two integers without using the modulo operator. The function should take two integers as input and return their GCD. Use the Euclidean algorithm to solve the problem.
"""

def gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The GCD of a and b.
    """
    while b != 0:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a - (a // b) * b
    return abs(a)