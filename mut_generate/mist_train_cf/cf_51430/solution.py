"""
QUESTION:
Write a function named `lcm` that takes three distinct integers `x`, `y`, and `z` as input and returns their least common multiple. The function should use the greatest common divisor (gcd) to optimize computational resources.
"""

import math

def lcm(x, y, z):
    temp = math.gcd(x, y)
    lcm = (x * y) // temp
    lcm = (lcm * z) // math.gcd(lcm, z)

    return lcm