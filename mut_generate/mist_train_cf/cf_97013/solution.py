"""
QUESTION:
Implement a function `binary_search(arr, target)` that searches for a target element in a sorted array `arr` with a time complexity of O(log n), where n is the number of elements in the array. The function should return the index of the target element if found, or -1 if not found. The array `arr` is sorted in ascending order, and the function should not use any built-in search functions or libraries.
"""

def entrance(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1