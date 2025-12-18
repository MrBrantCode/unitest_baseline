"""
QUESTION:
Write a recursive function `gcd(a, b)` that calculates the greatest common factor of two positive integers `a` and `b` without using the modulo operator, any built-in function to calculate remainders, loops, or helper functions.
"""

def entance(a, b):
    if a == b:  
        return a
    elif a > b:  
        return entance(a - b, b)
    else:  
        return entance(a, b - a)