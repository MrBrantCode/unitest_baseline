"""
QUESTION:
Write a function `product_except_self` that takes an array of integers as input and returns an array where each element is the product of all other elements except the element at the current index. The function should handle arrays containing zeros, and it must not use division by zero.
"""

from functools import reduce
from operator import mul

def product_except_self(nums):
    zero_count = nums.count(0)
    if zero_count > 1:
        return [0]*len(nums)
    elif zero_count == 1:
        product = reduce(mul, (x for x in nums if x != 0), 1)
        return [product if x == 0 else 0 for x in nums]
    else:
        product = reduce(mul, nums, 1)
        return [product//x for x in nums]