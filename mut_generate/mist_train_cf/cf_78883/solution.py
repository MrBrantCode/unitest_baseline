"""
QUESTION:
Write a function `lcm(a, b)` that calculates the Least Common Multiple (LCM) of two positive integers `a` and `b`. The function should return an integer value representing the LCM of `a` and `b`.
"""

def find_lcm(a, b):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x
    return a * b // gcd(a, b)