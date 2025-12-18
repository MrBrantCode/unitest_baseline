"""
QUESTION:
Implement a binary search function that works on a sorted array in descending order. The function should be named `binary_search` and should take four parameters: the array, the lowest index, the highest index, and the target value. The function should return the index of the target value if found, or -1 if not found. The input array will be sorted in descending order and may contain duplicate values.
"""

def binary_search(arr, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            high = mid - 1
        else:
            low = mid + 1
    return -1