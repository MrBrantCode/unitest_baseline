"""
QUESTION:
Write a function `gcd(a, b)` that takes two integers `a` and `b` as input and returns their greatest common divisor. Use this function to find the greatest common divisor of `2^1001 - 1` and `2^1012 - 1`.
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)