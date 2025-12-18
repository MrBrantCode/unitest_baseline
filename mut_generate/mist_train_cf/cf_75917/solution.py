"""
QUESTION:
Create a function named `extended_gcd` that takes two integers `a` and `b` as input and returns a tuple containing three values: the greatest common divisor (gcd) of `a` and `b`, and two integers `x` and `y` such that `ax + by = gcd(a, b)`. The function should implement the Extended Euclidean Algorithm.
"""

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)