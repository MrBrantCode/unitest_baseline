"""
QUESTION:
Implement the function `max_subarray_sum` that takes a list of integers `nums` and returns the maximum sum of a contiguous subarray within `nums`. The function should return the maximum possible sum.
"""

from typing import List

def max_subarray_sum(nums: List[int]) -> int:
    max_sum = float('-inf')
    current_sum = 0
    
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum