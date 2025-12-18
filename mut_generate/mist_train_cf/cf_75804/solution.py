"""
QUESTION:
Implement a function `gcd(a, b)` that calculates the Greatest Common Divisor of two integers `a` and `b` using the Euclidean algorithm. The function should return the absolute value of the GCD, allowing it to handle both positive and negative integers.
"""

def gcd(a, b):
    while(b != 0):
        t = a
        a = b
        b = t % b

    return abs(a)