"""
QUESTION:
Write a function `is_greater_than_k(max_sum, k, arr)` that takes in three parameters: `max_sum`, an integer representing the maximum sum allowed for a subarray, `k`, an integer representing the threshold for the number of subarrays, and `arr`, a list of integers representing the input array. The function should return `True` if the number of subarrays whose sum exceeds `max_sum` is greater than `k`, and `False` otherwise. The constraints are: 1 <= max_sum <= 10^9, 1 <= k <= 10^5, and 1 <= len(arr) <= 10^5.
"""

from typing import List

def entrance(max_sum: int, k: int, arr: List[int]) -> bool:
    subarray_count = 0
    _sum = 0
    for i in range(len(arr)):  
        _sum += arr[i]
        if _sum > max_sum:
            subarray_count += 1
            if subarray_count >= k:
                return True
            _sum = arr[i]
    subarray_count += 1  
    return subarray_count > k