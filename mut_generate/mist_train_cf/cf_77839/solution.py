"""
QUESTION:
Write a function `maxSumRangeQuery(nums, requests)` that takes two parameters, an array of integers `nums` and an array of `requests` where `requests[i] = [starti, endi]`. The function should return the maximum total product of all requests among all permutations of `nums`, modulo `10^9 + 7`. The function should also consider the constraints that the product of any two adjacent elements in the permutation should not exceed `10^5` and the product of any two elements in the permutation should not exceed `10^6`.
"""

from typing import List
from itertools import accumulate

def maxSumRangeQuery(nums: List[int], requests: List[List[int]]) -> int:
    MOD = 10**9 + 7
    freq = [0]*len(nums)
    for s, e in requests:
        freq[s] += 1
        if e+1 < len(nums):
            freq[e+1] -= 1
    freq = list(accumulate(freq))
    freq.sort()
    nums.sort()
    return sum(a*b for a, b in zip(nums, freq)) % MOD