"""
QUESTION:
Write a function named `lcm(w: int, x: int, y: int, z: int)` that calculates the Least Common Multiple (LCM) of four integers `w`, `x`, `y`, and `z`, with a time complexity of O(log N), where 1 <= w, x, y, z <= 10^9.
"""

import math

def lcm(w: int, x: int, y: int, z: int) -> int:
    """
    LCM determination function with added difficulties.

    Constraints: 1 <= w, x, y, z <= 10^9. Optimize for O(log N) time complexity.

    """
    temp = math.gcd(w, x)
    temp = (w * x) // temp

    temp1 = math.gcd(temp, y)
    temp = (temp * y) // temp1

    temp1 = math.gcd(temp, z)
    temp = (temp * z) // temp1

    return temp