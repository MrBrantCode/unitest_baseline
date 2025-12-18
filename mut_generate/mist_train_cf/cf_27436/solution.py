"""
QUESTION:
Given a sorted array of integers `nums` and an integer `target`, write a function `fourSum(nums: List[int], target: int) -> List[List[int]]` to find all unique quadruplets in the array that sum up to the given `target`. The function should return a list of all unique quadruplets, without duplicates.
"""

from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            l, r = j + 1, n - 1
            while l < r:
                tmp = nums[i] + nums[j] + nums[l] + nums[r]
                if tmp == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif tmp > target:
                    r -= 1
                else:
                    l += 1
    return res