"""
QUESTION:
Implement the function `findMaxLength(nums)` that finds the maximum length of a contiguous subarray with an equal number of 0s and 1s in a binary array `nums`, which contains at most 50,000 elements and only 0s and 1s. The function should return the length of the longest contiguous subarray with an equal number of 0s and 1s, or 0 if no such subarray exists.
"""

from typing import List

def findMaxLength(nums: List[int]) -> int:
    max_length = 0
    count = 0
    count_map = {0: -1}  
    for i in range(len(nums)):
        count += 1 if nums[i] == 1 else -1  
        if count in count_map:  
            max_length = max(max_length, i - count_map[count])
        else:
            count_map[count] = i  
    return max_length