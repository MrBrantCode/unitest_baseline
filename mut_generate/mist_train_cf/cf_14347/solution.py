"""
QUESTION:
Write a function named `gcd` that takes two integers `a` and `b` as input and returns their greatest common divisor. The function should have a time complexity of O(log(min(a,b))) and use constant space.
"""

def entance(a, b):
    if b == 0:
        return a
    return entance(b, a % b)