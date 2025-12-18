"""
QUESTION:
Write a function `gcd(a, b)` that calculates the greatest common divisor of two non-negative integers `a` and `b` without using any built-in mathematical functions or libraries, with a time complexity of O(log(min(a,b))). The function should take two integers as input and return their greatest common divisor.
"""

def calculate_gcd(a, b):
    # Base case
    if b == 0:
        return a
    
    # Recursive case
    return calculate_gcd(b, a % b)