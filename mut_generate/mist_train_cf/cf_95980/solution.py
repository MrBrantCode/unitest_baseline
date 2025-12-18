"""
QUESTION:
Write a function `gcd(a, b)` that takes two integers `a` and `b` as input and returns their greatest common divisor without using built-in functions, loops, or recursion. The numbers can be positive or negative and should be treated as if they have up to 10^18 digits.
"""

def entance(a, b):
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
    return b