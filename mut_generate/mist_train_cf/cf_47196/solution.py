"""
QUESTION:
Create a function `computeGCD` that takes two integers `a` and `b` as input and returns their greatest common divisor using the Euclidean algorithm.
"""

def computeGCD(a, b):
    """
    Compute the greatest common divisor of two integers using the Euclidean algorithm.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The greatest common divisor of a and b.
    """
    # Everything divides 0
    if (b == 0):
        return a
    else:
        # recursive function call
        return computeGCD(b, a % b)