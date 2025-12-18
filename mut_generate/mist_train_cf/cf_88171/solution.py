"""
QUESTION:
Create a function named `multiply` that takes two integer parameters `a` and `b` and returns their product without using the "*" operator or any other arithmetic operators.
"""

def multiply(a, b):
    result = 0
    if b < 0:
        a = -a
        b = -b
    
    while b != 0:
        if b & 1:
            result += a
        a <<= 1
        b >>= 1
    
    return result