"""
QUESTION:
You are given a strictly increasing array `nums` of distinct integers of length `n`. Implement the `findMissingNumber` function to find the smallest missing positive integer that does not appear in `nums`. The array `nums` is strictly increasing if for any index `i` where `1 <= i < nums.length`, the condition `nums[i - 1] < nums[i]` is satisfied. The function should take a list of integers as input and return the smallest missing positive integer. The length of the input list `nums` is between 1 and 10^5.
"""

def findMissingNumber(nums):
    n = len(nums)
    i = 0
    while i < n:
        if 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1