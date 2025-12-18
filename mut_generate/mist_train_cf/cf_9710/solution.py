"""
QUESTION:
Write a function `gcd(a, b)` that calculates the greatest common divisor of two integers `a` and `b` using an iterative method, without relying on built-in functions or libraries. The function should handle cases where `a` and `b` are not necessarily in order.
"""

def gcd(a, b):
    if a < b:
        a, b = b, a
    
    while b != 0:
        remainder = a % b
        a, b = b, remainder
    
    return a