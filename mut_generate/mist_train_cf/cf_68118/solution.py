"""
QUESTION:
Write a function `max_difference(nums: List[int]) -> int` that takes a chronological list of numbers as input and returns the greatest difference between any two numbers in the list, with the condition that the larger number must appear after the smaller one in the series. If the list is empty, return 0.
"""

from typing import List

def max_difference(nums: List[int]) -> int:
    if not nums:
        return 0

    max_diff = 0 
    min_val = nums[0] 

    for i in range(1, len(nums)):
        if nums[i] - min_val > max_diff:
            max_diff = nums[i] - min_val

        if nums[i] < min_val:
            min_val = nums[i]
    
    return max_diff