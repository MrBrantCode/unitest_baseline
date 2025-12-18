"""
QUESTION:
Given the array `nums` consisting of `n` positive integers, compute the sum of all non-empty continuous subarrays from the array, sort each subarray in non-decreasing order before summing up its elements, and then sort the sums in non-decreasing order, creating a new array of `n * (n + 1) / 2` numbers. Return the sum of the numbers from index `left` to index `right` (indexed from 1), inclusive, in the new array, modulo `10^9 + 7`.

The function should be named `range_sum_with_twist` and it should take three parameters: `nums`, `n`, and `left`, `right`. The length of `nums` is `n`, and `1 <= n <= 10^3`. Each element in `nums` is between `1` and `100`. `1 <= left <= right <= n * (n + 1) / 2`.
"""

from heapq import *

def range_sum_with_twist(nums, n, left, right):
    mod = 10**9 + 7
    h = []
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            heappush(h, -sum)
    
    for _ in range(n*(n+1)//2 - right):
        heappop(h)
    res = 0
    for _ in range(right - left + 1):
        res = (res - heappop(h)) % mod
    return res