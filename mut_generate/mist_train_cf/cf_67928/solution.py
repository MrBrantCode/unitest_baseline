"""
QUESTION:
Given an integer array `nums` and an integer `k`, return the maximum number of operations you can perform on the array where in one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array, with the restriction that you cannot remove the same pair more than once.
"""

def maxOperations(nums, k):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    res = 0
    for num in count:
        if k - num in count:
            res += min(count[num], count[k - num])

    return res // 2