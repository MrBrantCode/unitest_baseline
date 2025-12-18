"""
QUESTION:
Write a function `maxSumOfThreeSubarrays(nums, K)` that finds three non-overlapping subarrays with maximum sums in a given list `nums`, where each subarray has size `K`. The function should return the starting indices of the three subarrays in the form of a tuple `(i, j, k)`.

Restrictions: 
- The three subarrays cannot overlap.
- Each subarray must have size `K`.
"""

def maxSumOfThreeSubarrays(nums, K):
    W = [] 
    sum_ = 0
    for i, x in enumerate(nums):
        sum_ += x
        if i >= K: sum_ -= nums[i-K]
        if i >= K-1: W.append(sum_)

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
    for j in range(K, len(W) - K):
        i, k = left[j-K], right[j+K]
        if ans is None or (W[i] + W[j] + W[k] > 
        W[ans[0]] + W[ans[1]] + W[ans[2]]):
            ans = (i, j, k)
    return ans