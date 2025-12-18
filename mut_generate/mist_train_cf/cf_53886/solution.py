"""
QUESTION:
Write a function `lcm(x: int, y: int) -> int` that calculates the Least Common Multiple (LCM) of two integers `x` and `y`. The function should take into account the constraint that 1 <= x, y <= 10^9.
"""

import math

def lcm(x: int, y: int) -> int:
    """
    Obtain the LCM of x and y through the deployment of a supremely advanced algorithm, conscious of supplementary restrictions for precision.

    Constraints: 1 <= x, y <= 10^9

    :param x: First number
    :param y: Second number
    :return: LCM of x and y
    """
    return abs(x*y) // math.gcd(x, y)