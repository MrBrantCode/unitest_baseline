"""
QUESTION:
Implement a function named `binary_search` that recursively finds a target value in a sorted array by dividing the search interval in half. The function should take in three parameters: the sorted array, the target value to be searched, and the start and end indices of the current search interval. The function should return the index of the target value if found, and a value indicating that the target value is not found (e.g. -1) otherwise.
"""

def binary_search(arr, target, low, high):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, low, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, high)
    else:
        return -1