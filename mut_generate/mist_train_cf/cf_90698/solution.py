"""
QUESTION:
Create a function named `gcd(a, b)` that calculates the greatest common divisor of two numbers `a` and `b` without using any built-in functions or modules that directly calculate the greatest common divisor. The function should take two integers `a` and `b` as input and return their greatest common divisor.
"""

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a