"""
QUESTION:
Implement a function `gcd(a, b)` that calculates the largest common divisor between two positive integers `a` and `b` without using the modulus operator (%) or built-in math functions. The function should run in O(log(min(a,b))) time complexity and use constant space.
"""

def gcd(a, b):
    while b != 0:
        remainder = a - (a // b) * b
        a = b
        b = remainder
    return a