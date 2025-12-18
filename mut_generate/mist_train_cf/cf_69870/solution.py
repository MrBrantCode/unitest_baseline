"""
QUESTION:
Write a function named `splitArray(nums)` that takes an array of integers as input and returns a boolean value indicating whether there exist triplets (i, j, k) in the array such that the cumulative sum of the subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1), and (k + 1, n - 1) are identical, where 0 < i, i + 1 < j, j + 1 < k < n - 1. The input array has a length between 1 and 2000, and its elements are within the range [-1,000,000, 1,000,000].
"""

def splitArray(nums):
    n = len(nums)
    cum_sum = [0] * (n + 1)
    for i in range(n):
        cum_sum[i + 1] = cum_sum[i] + nums[i]
    for j in range(3, n - 3):
        sumSet = set()
        for i in range(1, j - 1):
            if cum_sum[i] == cum_sum[j] - cum_sum[i + 1]:
                sumSet.add(cum_sum[i])
        for k in range(j + 2, n - 1):
            if ((cum_sum[n] - cum_sum[k + 1] == cum_sum[k] - cum_sum[j + 1])
                and (cum_sum[k] - cum_sum[j + 1] in sumSet)):
                return True
    return False