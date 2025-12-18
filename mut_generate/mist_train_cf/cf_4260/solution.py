"""
QUESTION:
Implement a function `binary_search` that takes a sorted list of integers `arr` and a target integer `value` as input, and returns the index at which the value is found in the array, or the index at which it should be inserted to maintain the sorted order. The function should have the following signature: `binary_search(arr: List[int], value: int) -> int`. The input array has a length of at least 1 and at most 10^6, and the input value is between -10^9 and 10^9.
"""

from typing import List

def binary_search(arr: List[int], value: int) -> int:
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == value:
            return mid
        
        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    
    return left