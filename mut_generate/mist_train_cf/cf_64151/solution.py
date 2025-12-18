"""
QUESTION:
Design a function named 'lcm_list' that calculates the Least Common Multiple (LCM) of a list of integers. The function should accept a list of integers as arguments, where 1 <= len(numbers) <= 10^3 and 1 <= numbers[i] <= 10^6. The function should return the correct LCM of the input integers, ensuring an efficient and accurate algorithm is used.
"""

from typing import List
import math

def lcm_list(numbers: List[int]) -> int:
    lcm = numbers[0]
    for i in numbers[1:]:
        lcm = lcm*i//math.gcd(lcm, i)
    return lcm