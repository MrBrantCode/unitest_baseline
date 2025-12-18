"""
QUESTION:
Write a function `gcd` that takes two integers `a` and `b` as input and returns their greatest common divisor (GCD). The GCD should be computed using Stein's algorithm, which is an optimized version of the Euclidean algorithm that uses bitwise operations to reduce the number of iterations. The function should work correctly for all pairs of non-negative integers `(a, b)`, including cases where one or both of `a` and `b` are 0.
"""

def gcd(a, b):
    # Base cases
    if a == 0:
        return b
    if b == 0:
        return a

    # If both numbers are even
    if a % 2 == 0 and b % 2 == 0:
        return 2 * gcd(a // 2, b // 2)

    # If 'a' is even and 'b' is odd
    elif a % 2 == 0:
        return gcd(a // 2, b)

    # If 'a' is odd and 'b' is even
    elif b % 2 == 0:
        return gcd(a, b // 2)

    # If both numbers are odd
    else:
        return gcd(abs(a - b) // 2, min(a, b))