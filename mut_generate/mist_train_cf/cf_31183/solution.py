"""
QUESTION:
Implement a function `max_subarray_sum` that takes a list of integers as input and returns the maximum sum of a contiguous subarray within the list. The function should efficiently handle both positive and negative integers.
"""

from typing import List

def max_subarray_sum(nums: List[int]) -> int:
    max_sum = float('-inf')
    current_sum = 0
    
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum