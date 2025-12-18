"""
QUESTION:
Implement a function `gcd(a, b)` that calculates the greatest common divisor of two integers `a` and `b`. The function should not use any built-in library or function for finding the greatest common divisor. It should be able to handle large numbers efficiently and also handle negative numbers, returning the greatest common divisor as a positive number.
"""

def gcd(a, b):
    # Handle negative numbers
    a = abs(a)
    b = abs(b)
    
    # Base case: if b is 0, return a
    if b == 0:
        return a
    
    # Recursive step: find GCD of b and the remainder of dividing a by b
    return gcd(b, a % b)