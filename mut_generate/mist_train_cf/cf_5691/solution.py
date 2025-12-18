"""
QUESTION:
Given an array of integers and an integer K, find the maximum sum of a subarray with a length between 2 and K (inclusive). If the maximum sum is negative, return 0 instead. The array has a length between 2 and 10^5, and K is between 2 and the length of the array. 

Function signature: def max_subarray_sum(array: List[int], K: int) -> int.
"""

from typing import List

def max_subarray_sum(array: List[int], K: int) -> int:
    max_sum = 0
    current_sum = 0
    
    # Calculate the sum of the first K elements
    for i in range(K):
        current_sum += array[i]
    
    max_sum = max(max_sum, current_sum)
    
    # Calculate the sum of subarrays of length 2 to K
    for i in range(K, len(array)):
        current_sum += array[i] - array[i-K]
        current_sum = max(current_sum, 0)
        max_sum = max(max_sum, current_sum)
    
    return max_sum