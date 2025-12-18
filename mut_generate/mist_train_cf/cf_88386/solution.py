"""
QUESTION:
Implement a function `binary_search` that takes a sorted list of integers `arr` and an integer `value` as input, and returns the index at which the `value` is found in the array. If the `value` is not found, the function should return the index at which it should be inserted to maintain the sorted order.

The function should have the following signature: `def binary_search(arr: List[int], value: int) -> int`. 

The input constraints are: 
- `arr`: a sorted list of integers with length `n` (1 ≤ n ≤ 10^6)
- `value`: an integer (-10^9 ≤ value ≤ 10^9)
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