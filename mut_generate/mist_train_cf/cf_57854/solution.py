"""
QUESTION:
Given an array of integers `nums` and an integer `k`, implement a function `max_min_window(nums, k)` that returns a list of tuples, where each tuple contains the maximum and minimum values of a sliding window of size `k` moving from left to right over the array.

Constraints: `1 <= nums.length <= 10^5`, `-10^4 <= nums[i] <= 10^4`, and `1 <= k <= nums.length`.
"""

from typing import List, Tuple
from collections import deque

def max_min_window(nums: List[int], k: int) -> List[Tuple[int, int]]:
    n = len(nums)
    max_d, min_d = deque(), deque()
    result = []

    for i in range(n):
        while max_d and nums[i] >= nums[max_d[-1]]:
            max_d.pop()
        max_d.append(i)

        while min_d and nums[i] <= nums[min_d[-1]]:
            min_d.pop()
        min_d.append(i)

        if i >= k-1:
            result.append((nums[max_d[0]], nums[min_d[0]]))
            
            if i == max_d[0]:
                max_d.popleft()
                
            if i == min_d[0]:
                min_d.popleft()

    return result