"""
QUESTION:
Write a function named `gcd` that takes two integers `a` and `b` as input and returns their greatest common divisor (GCD) without using any built-in functions, loops, or recursion. The numbers can be positive or negative and are represented as integers.
"""

def gcd(a, b):
    # Convert to absolute values
    a = abs(a)
    b = abs(b)
    
    # Check for special cases
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Perform Euclidean algorithm
    while a != 0:
        if a >= b:
            a -= b
        else:
            b -= a
    
    # Return the GCD (absolute value of b)
    return abs(b)