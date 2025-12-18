"""
QUESTION:
Implement a function `lcm(a: int, b: int) -> int` that calculates the Least Common Multiple (LCM) of two integers `a` and `b`. The function should handle large inputs efficiently and return the LCM without errors. The inputs `a` and `b` are guaranteed to be positive integers in the range 1 to 10^6.
"""

import math

def lcm(a: int, b: int) -> int:
    return abs(a*b) // math.gcd(a, b)