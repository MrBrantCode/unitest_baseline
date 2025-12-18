"""
QUESTION:
Write a function `gcd(a, b)` to calculate the greatest common factor of two positive integers `a` and `b`. The function must use recursion and cannot use the modulo operator or any other built-in function to calculate remainders. Additionally, it cannot use any loops or helper functions.
"""

def gcd(a, b):
    if a == b:  
        return a
    elif a > b:  
        return gcd(a - b, b)
    else:  
        return gcd(a, b - a)