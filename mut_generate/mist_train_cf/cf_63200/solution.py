"""
QUESTION:
Write a function `lcm(w: int, x: int, y: int, z: int)` that calculates the Least Common Multiple (LCM) of four integers. The function should have a time complexity of O(log N), where N is the maximum of w, x, y, z. It should handle negative integers by returning an error message and ensure all inputs are within the range 1 <= w, x, y, z <= 1 billion.
"""

import math

def entrance(w: int, x: int, y: int, z: int) -> int:
    if min(w, x, y, z) < 1 or max(w, x, y, z) > 1e9: 
        return "Invalid inputs, numbers should be between 1 and one billion"
    lcm = w
    for i in [x, y, z]:
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm