"""
QUESTION:
Implement a function named `gcd` that calculates the greatest common divisor of two integers `a` and `b` without using any built-in GCD functions or libraries. The function should return the GCD of `a` and `b`.
"""

def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a