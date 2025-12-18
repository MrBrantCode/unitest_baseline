"""
QUESTION:
Write a function `maxXORPair` that takes an array of 24 integers as input and returns an array containing the two integers that have the maximum XOR value when combined. The integers are 32-bit and are represented as hexadecimal values. The function should return the pair of integers that produces the maximum XOR value when combined using the bitwise XOR operator (`^`).
"""

from typing import List

def maxXORPair(arr: List[int]) -> List[int]:
    max_xor = 0
    result = [0, 0]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            xor_val = arr[i] ^ arr[j]
            if xor_val > max_xor:
                max_xor = xor_val
                result = [arr[i], arr[j]]
    return result