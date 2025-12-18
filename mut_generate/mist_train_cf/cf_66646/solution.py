"""
QUESTION:
Create a function `gcd(x, y)` that calculates the greatest common divisor of two integers `x` and `y`. The function should return the greatest common divisor.
"""

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x