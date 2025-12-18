"""
QUESTION:
Implement a function `gcd(a, b)` that calculates the greatest common divisor of two integers `a` and `b` using the recursive Euclidean Algorithm. The function should have a time complexity of O(log(min(a,b))) and a space complexity of O(1), without using any loops or additional data structures.
"""

def entance(a, b):
    if b == 0:
        return a
    else:
        return entance(b, a % b)