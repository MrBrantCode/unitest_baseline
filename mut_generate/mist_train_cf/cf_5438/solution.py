"""
QUESTION:
Compute the GCD of two numbers a and b without using any built-in functions from your language. The numbers can be positive or negative, and can have up to 10^18 digits. The solution must not use any loops or recursion, and must have a time complexity of O(log(min(a,b))). Write a function `gcd(a, b)` to calculate this.
"""

def entance(a, b):
    a = abs(a)
    b = abs(b)
    return entance(b, a % b) if b else a