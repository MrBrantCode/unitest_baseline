"""
QUESTION:
Implement a function named `binary_search` that takes a sorted array `arr`, a target element `target`, and two indices `start` and `end` as input, and returns the index of the first occurrence of the target element in the array. The array may contain duplicate elements, and the function should have a time complexity of O(log n) where n is the size of the array. If the element is not found, the function should return -1.
"""

def binary_search(arr, target, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2

    if arr[mid] == target and (mid == 0 or arr[mid - 1] < target):
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr, target, start, mid - 1)