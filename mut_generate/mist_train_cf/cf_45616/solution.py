"""
QUESTION:
Write a function `lcm_of_three(a, b, c)` that calculates the least common multiple (LCM) of three unique integers `a`, `b`, and `c`. The function should take these integers as input and return their LCM as output. Note that `a`, `b`, and `c` are unique integers.
"""

import math

def lcm_of_three(a, b, c):
    def lcm(x, y):
        return abs(x*y) // math.gcd(x, y)
    return lcm(lcm(a, b), c)