"""
QUESTION:
Implement a function `binary_search_closest(arr, val)` that uses binary search to find the closest number to a given value `val` in a sorted array `arr`. If `val` is present in `arr`, return it. If there are two numbers equally close to `val`, return the smaller number. The function should take a sorted array `arr` and a target value `val` as input, and return the closest number in `arr` to `val`. The array `arr` is sorted in ascending order.
"""

def binary_search_closest(arr, val):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == val:
            return arr[mid]

        if arr[mid] < val:
            low = mid + 1
        else:
            high = mid - 1

    if low >= len(arr):
        return arr[high]
    elif high < 0:
        return arr[low]
    elif abs(arr[low] - val) <= abs(arr[high] - val):
        return arr[low]
    else:
        return arr[high]