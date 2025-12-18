"""
QUESTION:
Write a function `extended_euclidean(a, b)` that implements the Extended Euclidean algorithm to find the greatest common divisor and coefficients of Bézout's identity for two integers `a` and `b`. The function should return a tuple of three values: the greatest common divisor and the coefficients x and y such that ax + by = gcd(a, b).
"""

def extended_euclidean(a, b):
    # base case
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean(b % a, a)

        # update x and y
        temp = x
        x = y - (b // a) * x
        y = temp

        return gcd, x, y