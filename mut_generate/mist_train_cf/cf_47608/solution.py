"""
QUESTION:
Write a function named `lcm` that calculates the Least Common Multiple (LCM) of a list of integers. The list may contain up to 10^3 elements, each ranging from 1 to 10^9. The function should be optimized for performance.
"""

import math
from typing import List

def lcm(numbers: List[int]) -> int:
    """
    Calculate the LCM of a list of integers considering performance and specific constraints.

    Constraints: 1 <= length of list <= 10^3, 1 <= elements in list <= 10^9
    """
    lcm = 1
    for i in numbers:
        lcm = lcm*i//math.gcd(lcm, i)
    return lcm