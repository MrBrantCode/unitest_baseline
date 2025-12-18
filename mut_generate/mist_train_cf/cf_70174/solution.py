"""
QUESTION:
Write an efficient function named `lcm` that calculates the Least Common Multiple (LCM) of a given list of unique integers. The list can contain up to 10^3 elements, each ranging between 1 and 10^9 with no duplications.
"""

from typing import List
from math import gcd
from functools import reduce

def lcm(numbers: List[int]):
    """Calculate the LCM of a discrete list of integers considering optimization and certain constraints"""
    def lcm(a, b):
        """Calculate the Least Common Multiple of two integers."""
        return a * b // gcd(a, b)

    return reduce(lcm, numbers)