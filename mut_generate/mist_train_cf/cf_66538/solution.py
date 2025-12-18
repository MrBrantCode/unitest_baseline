"""
QUESTION:
Write a function `minKFlips` that takes a list of integers `A` and an integer `K` as input, and returns the minimum number of flips required to make all elements in the list the same. The flip operation is defined as flipping the subarray `A[i]` to `A[i+K-1]`. If it is impossible to make all elements the same, return -1. Assume that 1 represents the original value and 0 represents the flipped value.
"""

from typing import List

def minKFlips(A: List[int], K: int) -> int:
    N = len(A)
    hint = [0]*N
    flip = ans = 0
    
    for i in range(N): 
        flip ^= hint[i]
        if flip == A[i]:  
            ans += 1  
            flip ^= 1 
            if i + K < N:
                hint[i+K] ^= 1

    for i in range(N-K+1, N):
        flip ^= hint[i]
        if flip == A[i]: 
            return -1  
    return ans