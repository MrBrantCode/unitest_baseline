"""
QUESTION:
Implement the function `maximum_subarray_efficient(data)` that takes an array of integers `data` and returns the maximum subarray sum using a more efficient algorithm. The function should return the largest possible sum of a contiguous subarray within the input array. The input array may contain both positive and negative integers, and the function should handle cases where the input array contains only negative integers. The function should have a time complexity of O(n), where n is the length of the input array.
"""

from typing import List

def maximum_subarray_efficient(data: List[int]) -> int:
    max_sum = data[0]
    current_sum = data[0]

    for num in data[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum