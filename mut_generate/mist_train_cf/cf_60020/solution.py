"""
QUESTION:
Write a function named gcdex that takes two integers a and b as input and returns a tuple containing their greatest common divisor (GCD) and the coefficients x and y such that ax + by = gcd(a, b). The function should work correctly for all pairs of non-negative integers a and b, including cases where one or both of the inputs are 0.
"""

def gcdex(a: int, b: int):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = gcdex(b % a, a)
        return g, y - (b // a) * x, x