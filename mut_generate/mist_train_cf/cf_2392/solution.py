"""
QUESTION:
Create a function called `get_gcd` that takes two integers `a` and `b` as input, calculates their greatest common divisor using the Euclidean algorithm, and returns the result. The function should handle any integer values for `a` and `b`, including negative numbers, zero, and prime numbers. The time complexity of the function should be O(log(min(a, b))) and the space complexity should be O(log(min(a, b))).
"""

def get_gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The GCD of a and b.
    """
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a