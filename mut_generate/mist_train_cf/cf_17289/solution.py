"""
QUESTION:
Create a function called `gcd` that calculates the greatest common divisor of two positive integers using the Euclidean algorithm. The function should take two integers `a` and `b` as parameters, handle cases where `b` is 0, and have a time complexity of O(log(min(a, b))) and space complexity of O(log(min(a, b))).
"""

def gcd(a, b):
    """
    Calculate the greatest common divisor of two positive integers using the Euclidean algorithm.

    Args:
        a (int): The first positive integer.
        b (int): The second positive integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)