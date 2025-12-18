"""
QUESTION:
You are given an integer array `nums` and two integers `limit` and `goal`. The array `nums` has the property that `abs(nums[i]) &lt;= limit`. Return the minimum number of elements you need to add to make the sum of the array equal to `goal`. The added elements should be distinct and not already present in the array.
"""

from typing import List
import math

def minElements(nums: List[int], limit: int, goal: int) -> int:
    current_sum = sum(nums)
    remaining = abs(goal - current_sum)
    return math.ceil(remaining/limit)