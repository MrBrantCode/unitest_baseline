"""
QUESTION:
Create a function named `lcm(x, y, z)` that takes three integers `x`, `y`, and `z` as input and returns their least common multiple (LCM). Use the math.gcd() function from Python's built-in math module. The function should be able to handle any three positive integers.
"""

import math

def lcm(x, y, z):
    lcm_xy = x * y // math.gcd(x, y)
    return lcm_xy * z // math.gcd(lcm_xy, z)