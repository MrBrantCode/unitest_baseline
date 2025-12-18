"""
QUESTION:
Write a function `lcm(x, y)` that takes two lists `x` and `y` of positive integers as input and returns a list of the least common multiples (LCMs) for each pair of corresponding integers in `x` and `y`. The function should use a helper function `gcd(a, b)` to calculate the greatest common divisor of two integers `a` and `b`, and then use the formula `lcm(a, b) = |a*b| / gcd(a, b)` to calculate the LCM. The function should handle edge cases and optimize efficiency. The input lists `x` and `y` are of the same length and contain only positive integers.
"""

from typing import List

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def entance(x: List[int], y: List[int]) -> List[int]:
    lcm_vals = []
    for a, b in zip(x, y):  
        gcd_val = gcd(a, b)
        lcm_val = abs(a * b) // gcd_val  
        lcm_vals.append(lcm_val)
    return lcm_vals