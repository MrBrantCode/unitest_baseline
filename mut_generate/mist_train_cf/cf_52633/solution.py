"""
QUESTION:
Find the largest multiplier such that the sum of the multiplication results of the array elements rounded up to the nearest integer is less than or equal to the given threshold.

Function: findBestValue(nums, threshold)
Input: nums (list of integers), threshold (integer)
Output: largest multiplier (integer)
Restrictions: 1 <= len(nums) <= 5*10^4, 1 <= nums[i] <= 10^6, len(nums) <= threshold <= 10^6
"""

from typing import List
import math

def findBestValue(nums: List[int], threshold: int) -> int:
    l, r = 1, max(nums)
    while l < r:
        m = (l + r + 1) // 2
        if sum((n + m - 1) // m for n in nums) <= threshold:
            l = m
        else:
            r = m - 1
    return l