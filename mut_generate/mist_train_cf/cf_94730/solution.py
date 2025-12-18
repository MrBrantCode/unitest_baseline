"""
QUESTION:
Implement a binary search function that works with a descendingly sorted array. The function should take a sorted array, the start and end indices, and a target value as inputs and return the index of the target value if found, or -1 otherwise. The function should have a time complexity of O(log n).
"""

def entrance(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            end = mid - 1
        else:
            start = mid + 1
    return -1