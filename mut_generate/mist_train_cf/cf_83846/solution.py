"""
QUESTION:
Write a function `rangeSum(nums, n, left, right)` that takes an array `nums` of `n` positive integers, and two indices `left` and `right` as input, and returns the sum of the elements from index `left` to index `right` (indexed from 1) in a new array formed by sorting the sums of all non-empty continuous subarrays from `nums` in a non-decreasing order. The result should be returned modulo 10^9 + 7.

The constraints are: 1 <= n <= 10^3, 1 <= nums[i] <= 100, 1 <= left <= right <= n * (n + 1) / 2.
"""

import heapq

def rangeSum(nums, n, left, right):
    mod = 10**9 + 7
    pq = [(nums[i], i+1) for i in range(n)]
    heapq.heapify(pq)
    total = index = 0
    for _ in range(right):
        val, next_index = heapq.heappop(pq)
        if index >= left - 1:
            total = (total + val) % mod
        index += 1
        if next_index < n:
            new_val = val - nums[next_index - 1] + nums[next_index]
            heapq.heappush(pq, (new_val, next_index + 1))
    return total