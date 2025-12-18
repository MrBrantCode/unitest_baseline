"""
QUESTION:
Implement the `max_subarray_sum` function, which takes a list of integers as input and returns the maximum sum of a contiguous subarray within the input list. The function should find the contiguous subarray (containing at least one number) with the largest sum and return that sum. The function signature is `def max_subarray_sum(nums: List[int]) -> int:`
"""

from typing import List

def max_subarray_sum(nums: List[int]) -> int:
    max_sum = float('-inf')
    current_sum = 0
    
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum