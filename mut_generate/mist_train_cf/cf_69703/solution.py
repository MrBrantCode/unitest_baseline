"""
QUESTION:
Develop a function `get_lowest_common_multiple` that calculates the lowest common multiple (LCM) of an unrestricted number of positive integers provided as a list of integers. The function should return the LCM as an integer and handle any number of positive integers in the input list.
"""

from functools import reduce
from math import gcd
from typing import List

def get_lowest_common_multiple(list_of_ints: List[int]) -> int:
    def lcm(a, b):
        return abs(a*b) // gcd(a, b)

    return reduce(lcm, list_of_ints)