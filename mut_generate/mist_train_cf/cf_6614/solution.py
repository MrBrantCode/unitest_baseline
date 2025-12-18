"""
QUESTION:
Implement the `gcd` function to calculate the greatest common divisor of two integers `a` and `b` without using any built-in mathematical functions or libraries. The function should return the greatest common divisor of `a` and `b`.
"""

def gcd(a, b):
    """Returns the greatest common divisor of two numbers."""
    if a < b:
        a, b = b, a
    
    # Step 1: Check if both numbers are equal, in which case the greatest common divisor is the number itself
    if a == b:
        return a
    
    # Step 2: Check if one of the numbers is 0, in which case the other number is the greatest common divisor
    if b == 0:
        return a
    
    # Step 3: Find the greatest common divisor
    return gcd(b, a % b)