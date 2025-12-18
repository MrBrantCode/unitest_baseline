"""
QUESTION:
Write a function `minMoves(nums, k, m)` that takes an integer array `nums` consisting of only `0`'s and `1`'s, and two integers `k` and `m`, and returns the minimum number of moves required to have `k` consecutive `1`'s in `nums`. A move is a swap of two adjacent elements, but only allowed if the index of `1` is a multiple of `m`. If it's impossible to achieve `k` consecutive `1`'s, return `-1`. The constraints are `1 <= nums.length <= 10^5`, `nums[i]` is `0` or `1`, `1 <= k <= sum(nums)`, and `1 <= m <= nums.length`.
"""

from typing import List

def minMoves(nums: List[int], k: int, m: int) -> int:
    oneIndex = [i for i in range(len(nums)) if nums[i]==1]
    cnt = 0
    for i in range(len(oneIndex)-k+1):
        if oneIndex[i] % m != 0:
            continue
        x = oneIndex[i + k//2]
        j=k//2
        for _ in range(k):
            cnt += abs(oneIndex[i+j]-x) - abs(j)
            j = j-1 if j>0 else j+1
    return cnt if cnt > 0 else -1