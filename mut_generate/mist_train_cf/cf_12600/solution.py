"""
QUESTION:
Implement a function `gcd(a, b)` that calculates the greatest common factor of two positive integers `a` and `b`. The function should run in O(log(min(a, b))) time complexity.
"""

def gcd(a, b):
    # Ensure a is greater than b
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a