"""
QUESTION:
Write a function `sumOfSpecialEvenlySpacedElements(nums, queries)` that takes a 0-indexed integer array `nums` and an array `queries` where each element `queries[i]` is a pair `[xi, yi]`, and returns an array `answer` where `answer[i]` is the cumulative sum of all `nums[j]` where `xi` is less than or equal to `j` which is less than `n`, and the difference `(j - xi)` is divisible by `yi`, modulo `10^9 + 7`. The function should handle `1 <= n <= 5 * 10^4` and `1 <= queries.length <= 1.5 * 10^5`.
"""

def sumOfSpecialEvenlySpacedElements(nums, queries):
    prefix_sum = [0] * (len(nums) + 1)
    mod = 10**9 + 7
    for i in range(len(nums)):
        prefix_sum[i + 1] = (prefix_sum[i] + nums[i]) % mod

    result = []
    for xi, yi in queries:
        total = 0
        while xi < len(nums):
            total += nums[xi]
            total %= mod
            xi += yi
        result.append(total)
    return result