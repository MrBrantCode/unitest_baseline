"""
QUESTION:
Given a sorted array of integers `nums` in non-decreasing order, write a function `threeSum(nums)` that finds all unique triplets in the array that sum up to zero and returns them as a list of lists. Each triplet should be in non-decreasing order. The function should exclude duplicate triplets and handle inputs of length between 1 and 3000, with each integer in the range [-10^5, 10^5].
"""

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i - 1] == nums[i]: continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]: l += 1
                while l < r and nums[r] == nums[r - 1]: r -= 1
                l += 1
                r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res