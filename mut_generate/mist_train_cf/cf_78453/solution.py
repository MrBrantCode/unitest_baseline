"""
QUESTION:
Create a function named `solve` that takes a list of integers as input and returns a dictionary. The function should sort the input list into two subgroups: one containing multiples of 3 and the other containing non-multiples of 3. For each subgroup, calculate the sum of its elements and the least common multiple (LCM) of its elements. The function should return a dictionary with keys "subgroup1" and "subgroup2" containing dictionaries with keys "elements", "sum", and "least_common_multiple". If a subgroup is empty, the "least_common_multiple" value should be None.
"""

from math import gcd

def get_lcm(nums):
    lcm = nums[0]
    for i in range(1, len(nums)):
        lcm = lcm*nums[i] // gcd(lcm, nums[i])
    return lcm

def solve(lst):
    multiples = [i for i in lst if i % 3 == 0]
    non_multiples = [i for i in lst if i % 3 != 0]

    return {
        "subgroup1": {"elements": multiples,
                      "sum": sum(multiples),
                      "least_common_multiple": get_lcm(multiples) if multiples else None},
        "subgroup2": {"elements": non_multiples,
                      "sum": sum(non_multiples),
                      "least_common_multiple": get_lcm(non_multiples) if non_multiples else None}
    }