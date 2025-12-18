"""
QUESTION:
Implement a function `find_median(nums: List[int])` that takes a list of integers `nums` and returns the median of the list as a float. The median is the middle number when the list is sorted in ascending order. If the list has an even number of elements, the median is the average of the two middle numbers.
"""

from typing import List

def find_median(nums: List[int]) -> float:
    nums.sort()
    n = len(nums)
    if n % 2 == 0:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        return float(nums[n // 2])