"""
QUESTION:
Write a Python function `gcd(a, b)` to calculate the Greatest Common Divisor (GCD) of two integers `a` and `b` using only recursion without employing any built-in functions. The function should take two integer parameters `a` and `b` and return their GCD.
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)