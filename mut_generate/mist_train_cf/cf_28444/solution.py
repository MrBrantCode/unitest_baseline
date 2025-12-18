"""
QUESTION:
Write a function `countGoodPairs` that takes an array of integers `nums` and returns the number of pairs `(i, j)` where `nums[i] == nums[j]` and `i < j`. The function should have a time complexity of O(n), where n is the length of `nums`.
"""

from typing import List

def countGoodPairs(nums: List[int]) -> int:
    count = 0
    num_count = {}
    
    for num in nums:
        if num in num_count:
            count += num_count[num]
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    return count