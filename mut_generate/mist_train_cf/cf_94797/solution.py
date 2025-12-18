"""
QUESTION:
Write a function called `binary_search` that takes two parameters: a sorted list `arr` and an item `item`. The function should return the index of the first occurrence of `item` in `arr` using a binary search algorithm with a time complexity of O(log n). If `item` is not found, the function should return -1.
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
            # check if mid is the first occurrence
            if mid == 0 or arr[mid - 1] != item:
                return mid
            else:
                high = mid - 1
    
    return -1