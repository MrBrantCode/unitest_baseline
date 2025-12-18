"""
QUESTION:
Create a function called `gcd` that takes two integers `a` and `b` as input and returns their greatest common divisor (GCD) using the Euclidean algorithm, which continues to replace `a` with `b` and `b` with the remainder of `a` divided by `b` until `b` becomes 0.
"""

def gcd(a, b):
    while(b): 
        a, b = b, a % b
    return a