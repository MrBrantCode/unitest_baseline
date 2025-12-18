"""
QUESTION:
Develop a function named `lcm` that takes three strictly positive integers `x`, `y`, and `z` (1 ≤ x, y, z ≤ 10^5) as input and returns their least common multiple. The function should have a time complexity of O(log n), where n is the maximum of `x`, `y`, and `z`.
"""

import math

def lcm(x, y, z):
    lcm_xy = (x*y)//math.gcd(x,y)
    return (lcm_xy*z)//math.gcd(lcm_xy,z)