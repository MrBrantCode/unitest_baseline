"""
QUESTION:
Implement a recursive function `binary_search` that finds the first occurrence of a target element in a sorted array using the binary search algorithm. The function should take a sorted array `arr` and a target element `target` as input, and return the index of the first occurrence of the target element if it is present in the array, or -1 if it is not found. The function should have a time complexity of O(log n), where n is the length of the input array. The array may contain duplicates, and the function should be able to handle this case.
"""

from typing import List

def binary_search(arr: List[int], target: int) -> int:
    def binary_search_helper(arr: List[int], target: int, start: int, end: int) -> int:
        if start > end:
            return -1

        mid = (start + end) // 2

        if arr[mid] == target:
            if mid == 0 or arr[mid - 1] != target:
                return mid
            else:
                return binary_search_helper(arr, target, start, mid - 1)
        elif arr[mid] > target:
            return binary_search_helper(arr, target, start, mid - 1)
        else:
            return binary_search_helper(arr, target, mid + 1, end)

    return binary_search_helper(arr, target, 0, len(arr) - 1)