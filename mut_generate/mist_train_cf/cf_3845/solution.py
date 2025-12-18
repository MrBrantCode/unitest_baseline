"""
QUESTION:
Create a function named `multiply` that takes two integer parameters `a` and `b`. Implement the function to multiply `a` and `b` without using any arithmetic operators (+, -, *, /, %, etc.) and return the result.
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