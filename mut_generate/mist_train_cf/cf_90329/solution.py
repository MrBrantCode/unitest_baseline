"""
QUESTION:
Implement a function `gcd(a, b)` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean Algorithm, with a time complexity of O(log(min(a,b))) and a space complexity of O(1). The function should take two integer inputs and return their GCD.
"""

def gcd(a, b):
    """
    Calculate the greatest common divisor of two integers using the Euclidean Algorithm.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)