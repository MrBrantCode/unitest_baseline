"""
QUESTION:
Implement a function `combsum` that takes in a list of integers `nums` and an integer `target`. The function should return a list of all unique combinations of elements from `nums` that sum up to the `target`. The same number may be chosen from `nums` an unlimited number of times, and the order of combinations does not matter. The solution set must not contain duplicate combinations.
"""

from typing import List

def combsum(nums: List[int], target: int) -> List[List[int]]:
    if target == 0:
        return [[]]
    if not nums or nums[0] > target or target < 1:
        return []

    result = []
    nums.sort()

    def backtrack(remain, path, start):
        if remain < 0:
            return
        if remain == 0:
            result.append(path)
            return
        for i in range(start, len(nums)):
            backtrack(remain - nums[i], path + [nums[i]], i)

    backtrack(target, [], 0)
    return result