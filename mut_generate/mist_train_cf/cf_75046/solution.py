"""
QUESTION:
Write a function `gcd(a: int, b: int)` to calculate the Greatest Common Divisor (GCD) of two distinct prime numbers `a` and `b` with a time complexity of O(log min(a, b)). The constraints are 1 <= a, b <= 10^9, and `a` and `b` are distinct prime numbers.
"""

def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two distinct prime numbers a and b.

    Constraints: 1 <= a, b <= 10^9, and a, b are distinct prime numbers.

    :return: The GCD of a and b.
    """
    return 1