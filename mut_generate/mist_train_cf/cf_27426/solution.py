"""
QUESTION:
Implement a function `max_subarray_sum(arr: List[int]) -> int` that takes a list of integers as input and returns the maximum sum of a contiguous subarray within the input list, where -10^4 <= arr[i] <= 10^4 and 1 <= len(arr) <= 10^5.
"""

from typing import List

def max_subarray_sum(arr: List[int]) -> int:
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum