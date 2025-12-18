"""
QUESTION:
Create a function `maxSubarraySum` that takes an array of integers as input and returns the maximum sum of a subarray within that array. The function should efficiently handle large arrays. The maximum sum of a subarray is calculated by considering all possible contiguous blocks of elements within the original array.
"""

from typing import List

def maxSubarraySum(arr: List[int]) -> int:
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    current_sum = 0  # Initialize current_sum to 0

    for num in arr:
        current_sum = max(num, current_sum + num)  # Update current_sum to be the maximum of the current number and the sum of current_sum and the current number
        max_sum = max(max_sum, current_sum)  # Update max_sum to be the maximum of max_sum and current_sum

    return max_sum