"""
QUESTION:
Write a function `gcd(a, b)` that calculates the Greatest Common Divisor of two integers `a` and `b` without using any built-in functions. The function should work with positive and negative integers, and the integers can have up to 10^9 digits. The function should return the GCD of `a` and `b`.
"""

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a