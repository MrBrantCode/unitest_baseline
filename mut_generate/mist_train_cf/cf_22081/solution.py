"""
QUESTION:
Implement a function called `gcd(a, b)` that takes two numbers as parameters and returns their greatest common divisor without using any built-in library or function for finding the greatest common divisor. The function should be able to handle large numbers efficiently and return a positive result for both positive and negative input numbers.
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