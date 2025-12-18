"""
QUESTION:
Implement a function `gcd(a, b)` that calculates the Greatest Common Divisor of two numbers `a` and `b` without using any built-in GCD functions. The function should have a time complexity of O(log(min(a,b))) and be able to handle extremely large numbers with up to 1000 digits efficiently.
"""

def gcd(a, b):
    # Base case
    if b == 0:
        return a
    
    # Recursive case
    return gcd(b, a % b)