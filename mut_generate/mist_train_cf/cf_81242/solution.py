"""
QUESTION:
Write a function `lcm(w: int, x: int, y: int, z: int) -> int` that calculates the Least Common Multiple of four integers `w`, `x`, `y`, and `z`, where 1 <= w, x, y, z <= 10^9.
"""

import math

def lcm(w: int, x: int, y: int, z: int) -> int:
    lcm = w
    for i in [x, y, z]:
        lcm = (lcm * i)//math.gcd(lcm, i)
    return lcm