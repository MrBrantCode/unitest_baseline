"""
QUESTION:
Implement the `max_subarray_sum` function, which takes a list of integers as input and returns the maximum sum of a contiguous subarray within the list. The function should be able to handle both positive and negative integers.
"""

from typing import List

def max_subarray_sum(arr: List[int]) -> int:
    max_sum = float('-inf')  
    current_sum = 0  

    for num in arr:
        current_sum = max(num, current_sum + num)  
        max_sum = max(max_sum, current_sum)  

    return max_sum