"""
QUESTION:
Write a function `findUniqueCombinations` that takes a sorted list of integers `nums` and a target sum `target` as input, and returns a list of lists containing all unique combinations in `nums` that sum up to `target`. Each number in `nums` may only be used once in the combination, and the solution set must not contain duplicate combinations.
"""

from typing import List

def combinationSum2(nums: List[int], target: int) -> List[List[int]]:
    def backtrack(start, path, target):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            backtrack(i+1, path + [nums[i]], target - nums[i])
    
    nums.sort()
    result = []
    backtrack(0, [], target)
    return result