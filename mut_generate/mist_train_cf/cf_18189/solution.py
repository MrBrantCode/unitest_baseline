"""
QUESTION:
Write a function `gcd(a, b)` that calculates the Greatest Common Divisor of two numbers `a` and `b` without using any built-in GCD functions, achieving a time complexity of O(log(min(a,b))). The function should be able to handle extremely large numbers with up to 1000 digits.
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)