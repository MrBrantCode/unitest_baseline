"""
QUESTION:
Implement the `max_subarray_sum` function that takes a list of integers as input and returns the maximum sum of a subarray within the given array. A subarray is a contiguous segment of the array. The function should return an integer representing the maximum sum of any subarray.
"""

from typing import List

def max_subarray_sum(arr: List[int]) -> int:
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum