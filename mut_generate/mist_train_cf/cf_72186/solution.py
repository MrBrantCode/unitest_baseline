"""
QUESTION:
Write a function `lowest_common_multiple(x: List[int], y: List[int]) -> List[int]` that calculates the least common multiple (LCM) of each pair of positive integers `x` and `y` from two input lists. The function should assume that the two input lists are of the same length and each pair of integers corresponds to the same indices in both lists.
"""

from typing import List
from math import gcd

def lowest_common_multiple(x: List[int], y: List[int]) -> List[int]:
    return [abs(a*b) // gcd(a, b) for a, b in zip(x, y)]