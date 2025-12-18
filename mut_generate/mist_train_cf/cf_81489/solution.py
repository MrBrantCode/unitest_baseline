"""
QUESTION:
Write a function named `compute_gcd` that calculates the Greatest Common Divisor (GCD) of two positive integers. The function should take two parameters, `a` and `b`, and return the GCD of these integers.
"""

def compute_gcd(a, b):
    while(b):
        a, b = b, a % b
    return a