"""
QUESTION:
Write a function `minKBitFlips(A, K)` that takes an array `A` containing only 0s and 1s and an integer `K` as input, and returns the maximum number of K-bit flips possible so that there is no 1 in the array. If it is not possible, return `-1`. The length of `A` is at most 30000 and `K` is at least 1 and at most the length of `A`.
"""

from typing import List

def minKBitFlips(A: List[int], K: int) -> int:
    N = len(A)
    hint = [0] * N
    flip = ans = 0

    for i in range(N):
        flip ^= hint[i]
        if flip == A[i]:
            ans += 1
            flip ^= 1
            if i+K < N:
                hint[i+K] ^= 1

    for i in range(N-K+1, N):
        flip ^= hint[i]
        if flip == A[i]: return -1

    return ans