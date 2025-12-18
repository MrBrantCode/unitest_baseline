"""
QUESTION:
Implement a function `gcd(a, b)` that calculates the Greatest Common Divisor of two numbers `a` and `b` without using any built-in GCD functions. The function should have a time complexity of O(log(min(a,b))). The input `a` and `b` are integers, and the function should return their GCD.
"""

def gcd(a, b):
    # Base case: if b is 0, return a
    if b == 0:
        return a
    
    # Recursive case: call gcd recursively with b as the new a and the remainder of a divided by b as the new b
    return gcd(b, a % b)