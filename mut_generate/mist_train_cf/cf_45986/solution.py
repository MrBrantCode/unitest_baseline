"""
QUESTION:
Develop a function max_min_product that takes a list of integers as input and returns a tuple of two integers. The function should find the maximum and minimum product of a sub-array within the input list, considering all possible sub-arrays and handling negative numbers and zeroes appropriately. The function should return the maximum product as the first element of the tuple and the minimum product as the second element.
"""

from typing import List, Tuple

def max_min_product(nums: List[int]) -> Tuple[int, int]:
    max_product_global = nums[0]
    min_product_global = nums[0]
    max_product_local = nums[0]
    min_product_local = nums[0]

    for i in range(1, len(nums)):
        temp = max_product_local
        max_product_local = max(nums[i], max_product_local * nums[i], min_product_local * nums[i])
        min_product_local = min(nums[i], temp * nums[i], min_product_local * nums[i])

        if max_product_local > max_product_global:
            max_product_global = max_product_local

        if min_product_local < min_product_global:
            min_product_global = min_product_local

    return (max_product_global, min_product_global)