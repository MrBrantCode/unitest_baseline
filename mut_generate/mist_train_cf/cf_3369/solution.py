"""
QUESTION:
Implement a function `gcd(a, b)` to find the Greatest Common Divisor (GCD) of two numbers `a` and `b` without using any built-in GCD functions, with a time complexity of O(log(min(a,b))). The function should be able to handle extremely large numbers with up to 1000 digits efficiently.
"""

def gcd(a, b):
    # Base case
    if b == 0:
        return a
    
    # Recursive case
    return gcd(b, a % b)