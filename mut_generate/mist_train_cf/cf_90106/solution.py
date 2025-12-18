"""
QUESTION:
Implement the `gcd` function to calculate the greatest common divisor of two integers `a` and `b` in O(log(min(a,b))) time complexity and constant space, without using the modulus operator (%) or any built-in math functions. The function should handle negative inputs and return the GCD as a positive integer.
"""

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    
    while b:
        a, b = b, a - (a // b) * b
    
    return a