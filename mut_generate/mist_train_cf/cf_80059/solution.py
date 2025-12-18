"""
QUESTION:
Compose a function 'array_lcm' that accepts an array of integers as input and returns their Least Common Multiple through an efficient algorithm. The input array contains 1 to 10^3 integers, each ranging from 1 to 10^9.
"""

from typing import List
from math import gcd

def array_lcm(arr: List[int]) -> int:
    """Compute the Least Common Multiple (LCM) of an array of integers using an efficient algorithm."""  
    lcm = arr[0]
    for i in arr[1:]:
        lcm = abs(lcm*i) // gcd(lcm, i)
    return lcm