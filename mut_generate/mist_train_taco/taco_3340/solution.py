"""
QUESTION:
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:


Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:


Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

def find_target_range(nums, target):
    def first_greater_equal(nums, target):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    start = first_greater_equal(nums, target)
    if start == len(nums) or nums[start] != target:
        return [-1, -1]
    
    end = first_greater_equal(nums, target + 1) - 1
    return [start, end]