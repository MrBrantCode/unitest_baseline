"""
QUESTION:
Write a function `findMaxLength` that takes an array of integers as input where each element is either 0 or 1, and returns the length of the longest contiguous subarray with an equal number of 0s and 1s.
"""

from typing import List

def findMaxLength(nums: List[int]) -> int:
    max_len = 0
    rolling_sum = 0
    seen_sums = {0: -1}

    for i, num in enumerate(nums):
        if num == 0:
            rolling_sum -= 1
        else:
            rolling_sum += 1

        if rolling_sum in seen_sums:
            max_len = max(max_len, i - seen_sums[rolling_sum])
        else:
            seen_sums[rolling_sum] = i

    return max_len