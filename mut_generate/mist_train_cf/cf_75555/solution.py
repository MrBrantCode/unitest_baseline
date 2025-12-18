"""
QUESTION:
You are given two arrays: a 2D integer array `groups` with `n` subarrays, and a 1D integer array `nums`. Implement a function `canChoose(groups, nums)` that determines if it is possible to select `n` disjoint subarrays from `nums` such that the `ith` subarray corresponds to `groups[i]` and the `(i-1)th` subarray precedes the `ith` subarray in `nums`. Return `True` if this is possible and `False` otherwise.

The constraints are: `groups.length == n`, `1 <= n <= 103`, `1 <= groups[i].length, sum(groups[i].length) <= 103`, `1 <= nums.length <= 103`, and `-107 <= groups[i][j], nums[k] <= 107`.
"""

def canChoose(groups, nums):
    j = 0
    for group in groups:
        while j <= len(nums)-len(group):
            if nums[j:j+len(group)] == group:
                j += len(group)
                break
            j += 1
        else:
            return False
    return True