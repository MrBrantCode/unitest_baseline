"""
QUESTION:
Write a function `count_set_bits(num)` that takes a positive integer `num` as input and returns a list of integers representing the count of set bits (binary 1s) for each number from 0 to `num`, inclusive. The function should return a list of length `num + 1` where each element at index `i` represents the count of set bits in the binary representation of `i`.
"""

from typing import List

def count_set_bits(num: int) -> List[int]:
    ans = [0] * (num + 1)
    for i in range(1, num + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans