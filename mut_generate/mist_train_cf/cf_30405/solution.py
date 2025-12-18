"""
QUESTION:
Write a function `max_non_decreasing_subarray_length` that takes a list of integers `A` and returns the length of the longest contiguous non-decreasing subarray within `A`. The function should return an integer value. The input list `A` can contain any integers, and the function should return 1 if no non-decreasing subarray of length greater than 1 is found.
"""

from typing import List

def max_non_decreasing_subarray_length(A: List[int]) -> int:
    result = 1
    current_length = 1
    for i in range(1, len(A)):
        if A[i] >= A[i-1]:
            current_length += 1
        else:
            result = max(result, current_length)
            current_length = 1
    return max(result, current_length)