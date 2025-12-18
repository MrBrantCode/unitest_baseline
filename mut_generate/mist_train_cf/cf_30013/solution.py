"""
QUESTION:
Write a function `find_equilibrium_index` that takes a list of integers `arr` as input and returns the equilibrium index of the array. The equilibrium index is any integer `i` such that the sum of elements at indices less than `i` is equal to the sum of elements at indices greater than `i`. If no equilibrium index exists, return -1. The function should have the signature `find_equilibrium_index(arr: List[int]) -> int`.
"""

from typing import List

def find_equilibrium_index(arr: List[int]) -> int:
    total_sum = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        total_sum -= arr[i]
        if left_sum == total_sum:
            return i
        left_sum += arr[i]
    return -1