"""
QUESTION:
Implement a function `binary_search_closest(arr, target)` that uses binary search to find the closest number to a given `target` value in a sorted array `arr`. If `target` is present in `arr`, return it as the closest number. If there are two numbers equally close to `target`, return the larger number. The array `arr` can have duplicate values, a maximum length of 10^6, and can be sorted in ascending or descending order.
"""

def binary_search_closest(arr, target):
    low = 0
    high = len(arr) - 1
    closest = None

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return arr[mid]

        if closest is None or abs(arr[mid] - target) < abs(closest - target):
            closest = arr[mid]
        elif abs(arr[mid] - target) == abs(closest - target) and arr[mid] > closest:
            closest = arr[mid]

        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return closest