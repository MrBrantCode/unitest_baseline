"""
QUESTION:
Write a function `combination_sum` that takes a list of positive integers `nums` and a target sum `target` as input, and returns all unique combinations in `nums` that sum up to `target`. Each number in `nums` may only be used once in the combination, and the solution set must not contain duplicate combinations.
"""

from typing import List

def combination_sum(nums: List[int], target: int) -> List[List[int]]:
    def backtrack(start, target, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            backtrack(i+1, target-nums[i], path+[nums[i]], res)
    
    nums.sort()
    res = []
    backtrack(0, target, [], res)
    return res