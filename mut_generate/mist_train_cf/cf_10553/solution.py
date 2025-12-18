"""
QUESTION:
Create a function `gcd` that takes two positive integers `a` and `b` as input and returns their greatest common divisor using the Euclidean algorithm. Implement a recursive version of the algorithm.
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)