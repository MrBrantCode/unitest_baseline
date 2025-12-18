"""
QUESTION:
Write a function `maxOperations(nums, k, d)` that takes an integer array `nums`, an integer `k`, and an integer `d` as input, and returns the maximum number of operations that can be performed on the array. In one operation, two numbers from the array whose sum equals `k` and are at least `d` distance apart can be removed from the array. The length of `nums` is between 1 and 10^5 (inclusive), each element in `nums` is between 1 and 10^9 (inclusive), `k` is between 1 and 10^9 (inclusive), and `d` is between 1 and the length of `nums` (inclusive).
"""

def maxOperations(nums, k, d):
    nums.sort()
    left, right = 0, len(nums) - 1
    operationCount = 0
    while left + d <= right:
        if nums[left] + nums[right] == k:
            operationCount += 1
            left += 1
            right -= 1
        elif nums[left] + nums[right] > k:
            right -= 1
        else:
            left += 1
    return operationCount