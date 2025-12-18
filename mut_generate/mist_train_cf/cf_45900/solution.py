"""
QUESTION:
Define a function `rangeSum(nums, n, left, right)` that takes an array `nums` of `n` positive integers, and two integers `left` and `right` as input. The function should calculate the sum of all non-empty continuous subarrays from the array, sort these sums in non-decreasing order, and return the sum of the numbers from index `left` to index `right` (indexed from 1), inclusive, in the new array, modulo 10^9 + 7.

Restrictions:
- `1 <= nums.length <= 10^3`
- `nums.length == n`
- `1 <= nums[i] <= 100`
- `1 <= left <= right <= n * (n + 1) / 2`
"""

import heapq

def rangeSum(nums, n, left, right):
    mod = 10**9 + 7
    prefixSums = [0] + nums[:]
    for i in range(1, len(prefixSums)):
        prefixSums[i] += prefixSums[i - 1]
    sumsArray = []
    for i in range(n):
        for j in range(i+1, n+1):
            heapq.heappush(sumsArray, (prefixSums[j] - prefixSums[i]))

    result = 0
    for i in range(1, right + 1):
        if i >= left:
            result = (result + heapq.heappop(sumsArray)) % mod
        else:
            heapq.heappop(sumsArray)
    return result