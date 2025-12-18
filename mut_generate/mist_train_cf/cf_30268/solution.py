"""
QUESTION:
Implement a function `cumulative_sum` that takes a list of integers as input and returns a new list containing the cumulative sum of the input list. The cumulative sum at each index in the output list should be the sum of all the integers from the input list up to and including the integer at that index. The input list will contain at least one integer, and the output list should have the same length as the input list.
"""

from typing import List

def cumulative_sum(nums: List[int]) -> List[int]:
    cumulative = []
    total = 0
    for num in nums:
        total += num
        cumulative.append(total)
    return cumulative