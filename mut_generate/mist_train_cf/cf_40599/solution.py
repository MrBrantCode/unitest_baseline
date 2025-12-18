"""
QUESTION:
Implement a function `countBits_alternative` that takes a non-negative integer `num` as input and returns an array `dp` of size `num+1`, where `dp[i]` represents the number of 1 bits in the binary representation of `i` for all `0 <= i <= num`. Do not use bitwise operations. The function should return an array where each element `dp[i]` is the count of 1 bits in the binary representation of `i`.
"""

from typing import List

def countBits(num: int) -> List[int]:
    dp = [0] * (num+1)
    for i in range(num+1):
        dp[i] = bin(i).count('1')
    return dp