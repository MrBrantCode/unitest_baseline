"""
QUESTION:
Write a function `lcm` that calculates the Least Common Multiple (LCM) of multiple numbers in a list. The function should ignore any invalid entries in the list, which are non-integer or negative numbers. The list may contain up to 10^6 integers and each integer is in the range of 1 to 10^9. The function should be efficient enough to process the list in a reasonable time.
"""

from typing import List
import math

def lcm_list(l: List[int]) -> int:
    # calculate GCD
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # calculate LCM
    def calc_lcm(a, b):
        return a * b // gcd(a, b)

    lcm_val = 1
    for i in l:
        if isinstance(i, int) and i > 0:
            lcm_val = calc_lcm(lcm_val, i)
    return lcm_val