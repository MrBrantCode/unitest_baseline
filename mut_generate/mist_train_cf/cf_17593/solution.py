"""
QUESTION:
Create a function called `binary_search` that takes a sorted list `arr` and an item `item` as parameters and returns the index of the first occurrence of `item` in `arr` using a binary search algorithm with a time complexity of O(log n). If `item` is not found in `arr`, the function should return -1.
"""

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < item:
            low = mid + 1
        elif arr[mid] > item:
            high = mid - 1
        else:
            return mid
    
    return -1