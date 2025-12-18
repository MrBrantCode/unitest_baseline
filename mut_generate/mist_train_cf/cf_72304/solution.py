"""
QUESTION:
Given an array with n integers, write a function `splitArray(nums)` that determines if there are quadruplets (i, j, k, l) which satisfy the conditions: 
0 < i, i + 1 < j, j + 1 < k, k + 1 < l < n - 1 and the sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1), (k + 1, l - 1) and (l + 1, n - 1) are equal.

Restrictions: 1 <= n <= 5000 and elements in the given array will be in range [-1,000,000, 1,000,000].
"""

def splitArray(nums):
    total = sum(nums)
    s1 = 0
    dict_j = {}
    for j in range(1, len(nums) - 1):
        s1 += nums[j - 1]
        if s1 * 2 + nums[j] == total:
            dict_j[s1] = j
    s4 = 0
    for l in range(len(nums) - 2, 1, -1):
        s4 += nums[l + 1]
        if s4 * 2 + nums[l] == total:
            if s4 in dict_j:
                return True
    return False