"""
QUESTION:
Implement a recursive function called `binary_search` that finds the index of a target element in a sorted array using the binary search algorithm. The function should take a sorted array of integers and a target integer as input, and return the index of the target element if it is present in the array, or -1 if it is not found. The input array is assumed to be sorted in ascending order and does not contain any duplicates.
"""

from typing import List

def binary_search(arr: List[int], target: int) -> int:
    def binary_search_helper(start: int, end: int) -> int:
        if start > end:
            return -1
        
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return binary_search_helper(start, mid - 1)
        else:
            return binary_search_helper(mid + 1, end)
    
    return binary_search_helper(0, len(arr) - 1)