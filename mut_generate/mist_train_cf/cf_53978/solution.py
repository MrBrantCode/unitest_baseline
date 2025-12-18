"""
QUESTION:
Implement the `binary_search` function to find an element `x` in a sorted array `arr`. The function should return the index of `x` if found, otherwise return `None`. The array is guaranteed to be sorted in ascending order.
"""

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return None