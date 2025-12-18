"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a recursive binary search for a target element in a sorted array `arr`. The function should return `True` if the target is found and `False` otherwise. The time complexity should be O(log n) and the space complexity should be O(log n), where n is the size of the array.
"""

def binary_search(arr, target):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            return binary_search(arr[mid+1:], target)
        else:
            return binary_search(arr[:mid], target)