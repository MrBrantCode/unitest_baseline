"""
QUESTION:
Write a function `lcm(numbers: list)` that calculates the Least Common Multiple (LCM) of `n` positive non-zero integers. The function should take a list of integers as input, where each integer is between 1 and 10^9, and the length of the list is between 1 and 10^6. The function should be optimized for time complexity.
"""

import math
from functools import reduce

def lcm(numbers: list) -> int:
    return reduce(lambda x, y: x*y // math.gcd(x, y), numbers)