"""
QUESTION:
Write a function `numSubarrayProductLessThanK(nums, k)` that calculates the number of contiguous subarrays in `nums` where the product of all the elements within the subarray is strictly less than `k`. 

`nums` is an array of positive integers with a length greater than 0 and less than or equal to 50000, and each element is greater than 0 and less than 1000. `k` is a value greater than or equal to 0 and less than 10^6.
"""

from typing import List

def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0
    l = 0
    count = 0
    product = 1
    for r in range(len(nums)):
        product *= nums[r]
        while product >= k:
            product /= nums[l]
            l += 1
        count += r - l + 1
    return count