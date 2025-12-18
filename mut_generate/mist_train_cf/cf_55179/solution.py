"""
QUESTION:
Calculate the least common multiple (LCM) and the greatest common divisor (GCD) for each distinct pair of numbers in a given list of up to 100 integers. Implement a function that takes a list of integers as input and returns a dictionary where the keys are tuples representing distinct pairs of numbers and the values are tuples containing the LCM and GCD of the numbers in the key tuple. Use an efficient algorithm to calculate the LCM and GCD, and consider cases where the Python version is less than 3.9, which lacks the built-in lcm function in the math module.
"""

import math
from itertools import combinations

def entrance(lst):
    result = {}
    for nums in combinations(lst, 2):
        lcm = math.lcm(nums[0], nums[1]) if hasattr(math, 'lcm') else abs(nums[0]*nums[1]) // math.gcd(nums[0], nums[1])
        gcd = math.gcd(nums[0], nums[1])
        result[nums] = (lcm, gcd)
    return result