"""
QUESTION:
Write a function `lowest_common_multiple(numbers_list)` that calculates the lowest common multiple (LCM) of a given list of integers. The list can contain up to 1000 numbers and the function should be optimized for handling large numbers.
"""

import math

def lowest_common_multiple(numbers_list):
    lcm = numbers_list[0]
    for i in range(1,len(numbers_list)):
        lcm = lcm*numbers_list[i]//math.gcd(lcm, numbers_list[i])
    return lcm