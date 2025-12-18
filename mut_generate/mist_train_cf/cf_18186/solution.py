"""
QUESTION:
Create a function `gcd(a, b)` that calculates the greatest common divisor of two positive integers `a` and `b` with a time complexity of O(log(min(a,b))) and a space complexity of O(1).
"""

def gcd(a, b):
    # Ensure a is always greater than or equal to b
    if a < b:
        a, b = b, a
    
    # Perform Euclidean algorithm to find GCD
    while b != 0:
        a, b = b, a % b
    
    return a