"""
QUESTION:
Given an array `nums` of positive integers and an integer `k`, write a function `maxSumOfThreeSubarrays` that finds three non-overlapping subarrays of length `k` with the maximum sum. The function should return a list of starting indices of these subarrays. If there are multiple correct answers, return the lexicographically smallest one.

Constraints: The length of `nums` is between 1 and 20000, each `nums[i]` is between 1 and 65535, and `k` is between 1 and the floor value of `nums.length / 3`.
"""

def maxSumOfThreeSubarrays(nums, k):
    W = [] 
    N = len(nums)
    sum_ = 0
    for i, x in enumerate(nums):
        sum_ += x
        if i >= k: sum_ -= nums[i-k]
        if i >= k-1: W.append(sum_)

    left = [0] * len(W)
    best = 0
    for i in range(len(W)):
        if W[i] > W[best]:
            best = i
        left[i] = best

    right = [0] * len(W)
    best = len(W) - 1
    for i in range(len(W) - 1, -1, -1):
        if W[i] >= W[best]:
            best = i
        right[i] = best

    ans = None
    for j in range(k, len(W) - k):
        i, l = left[j-k], right[j+k]
        if ans is None or (W[i] + W[j] + W[l] > 
                           W[ans[0]] + W[ans[1]] + W[ans[2]]):
            ans = i, j, l
    return ans