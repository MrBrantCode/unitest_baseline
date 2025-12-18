"""
QUESTION:
Implement a function `gcd(a, b)` that calculates the greatest common divisor of two positive integers `a` and `b`, where 1 <= a, b <= 10^9, without using any built-in GCD functions or libraries.
"""

def gcd(a, b):
    # base case: if b is 0, then gcd(a, b) = a
    if b == 0:
        return a
    else:
        # recursively find the gcd of b and the remainder of a divided by b
        return gcd(b, a % b)