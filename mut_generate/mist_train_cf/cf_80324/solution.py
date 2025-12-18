"""
QUESTION:
Create a function called `lcm` that takes three integers `x`, `y`, and `z` as input, where 1 <= x, y, z <= 10^9, and returns their lowest common multiple (LCM) using an efficient algorithm.
"""

import math

def lcm(x: int, y: int, z: int) -> int:
    """
    Determine the LCM of x, y and z using a highly efficient algorithm, taking extra constraints into account.

    Bounds: 1 <= x, y, z <= 10^9
    """
    temp = (x*y) // math.gcd(x,y)
    return (temp*z) // math.gcd(temp,z)