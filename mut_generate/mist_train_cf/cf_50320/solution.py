"""
QUESTION:
Create a function called `gcd` that calculates and returns the Greatest Common Divisor of two integers `a` and `b`.
"""

def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a