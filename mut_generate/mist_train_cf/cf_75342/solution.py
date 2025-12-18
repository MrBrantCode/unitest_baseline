"""
QUESTION:
Given a 2D integer array `groups` of length `n` and an integer array `nums`, determine if it's possible to choose `n` disjoint subarrays from `nums` that are equal to the subarrays in `groups`, in the same order. Return `True` if possible and the starting and ending indices of each subarray in `nums`; otherwise, return `False` and an empty array.

Restrictions: `groups.length == n`, `1 <= n <= 103`, `1 <= groups[i].length, sum(groups[i].length) <= 103`, `1 <= nums.length <= 103`, `-107 <= groups[i][j], nums[k] <= 107`. The function should be named `check_subarrays` and take `groups` and `nums` as parameters.
"""

def canChoose(groups, nums):
    ans = []
    j = 0
    for i, group in enumerate(groups):
        group_len = len(group)
        while j + group_len - 1 < len(nums):
            if nums[j:j+group_len] == group:
                ans.append([j, j+group_len-1])
                j += group_len
                break
            else:
                j += 1
        else:
            return False 
    return True and ans