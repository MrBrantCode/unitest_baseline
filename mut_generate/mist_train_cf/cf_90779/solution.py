"""
QUESTION:
Implement a function `hcf(a, b)` that calculates the highest common factor of two given numbers `a` and `b` using only bitwise operators and without using any arithmetic operators.
"""

def hcf(a, b):
    if a == 0:
        return b
    
    if b == 0:
        return a
    
    # Find the greatest power of 2 that divides both a and b
    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1
    
    # Remove all powers of 2 from a
    while (a & 1) == 0:
        a >>= 1
    
    # Now a is odd
    while b != 0:
        # Remove all powers of 2 from b
        while (b & 1) == 0:
            b >>= 1
        
        # If a > b, swap them
        if a > b:
            a, b = b, a
        
        # Subtract smaller number from larger number
        b = (b - a)
    
    # Restore common factors of 2
    return a << shift