"""
QUESTION:
Implement a function `gcd(a, b)` that calculates the greatest common divisor of two integers `a` and `b`. The function should have a time complexity of O(log(min(a,b))) and use constant space. It should also handle negative inputs and return the GCD as a positive integer, without using the modulus operator (%) or any built-in math functions such as sqrt() or pow().
"""

def gcd(a, b):
    # Handle negative inputs
    a = abs(a)
    b = abs(b)
    
    # Base cases
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Reduce the problem to a smaller one
    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)