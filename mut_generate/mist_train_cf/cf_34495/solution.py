"""
QUESTION:
Implement a function `transform_sequence(a)` that takes a list of integers `a` as input, applies a transformation to each element in the list, and returns the resulting list of transformed integers. The transformation involves performing the following bitwise operations on each element `a[i]`: `a[i] = a[i] ^ (a[i] << 1) ^ (a[i] & (a[i] << 1)) ^ (a[i] & (a[i] << 1) & (a[i] << 2))`. The function should return a list of integers, where each integer is the result of the transformation applied to the corresponding element in the input list.
"""

from typing import List

def transform_sequence(a: List[int]) -> List[int]:
    return [num ^ (num << 1) ^ (num & (num << 1)) ^ (num & (num << 1) & (num << 2)) for num in a]