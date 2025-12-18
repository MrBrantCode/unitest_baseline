"""
QUESTION:
Implement the `max_subarray_sum` function to find the maximum sum of a contiguous subarray within the input list of integers. The function should take a list of integers as input and return the maximum sum of a contiguous subarray.
"""

from typing import List

def max_subarray_sum(arr: List[int]) -> int:
    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum