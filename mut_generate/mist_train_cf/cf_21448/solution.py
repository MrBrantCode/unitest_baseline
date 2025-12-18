"""
QUESTION:
Write a function `gcd(a, b)` that calculates the greatest common factor of two positive integers `a` and `b` using recursion, without using the modulo operator or any other built-in function to calculate remainders.
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a - b * (a // b))