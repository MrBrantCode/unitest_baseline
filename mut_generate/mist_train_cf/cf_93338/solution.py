"""
QUESTION:
Write a function `gcd(a, b)` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean Algorithm with a time complexity of O(log(min(a,b))) and a space complexity of O(1).
"""

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    
    while b != 0:
        r = a % b
        a = b
        b = r
    
    return a