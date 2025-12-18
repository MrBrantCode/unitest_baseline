"""
QUESTION:
Create a function `smallest_common_multiple(lst)` that takes a list of integers `lst` and returns the smallest common multiple of all the numbers in the list. The function should calculate the greatest common divisor (GCD) of each pair of integers, then use these to find the least common multiple (LCM). The input list will contain at least two integers.
"""

import math
from functools import reduce

def smallest_common_multiple(lst):
    def find_lcm(num1, num2):
        return (num1*num2) // math.gcd(num1, num2)

    return reduce(find_lcm, lst)