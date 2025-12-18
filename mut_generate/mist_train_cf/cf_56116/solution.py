"""
QUESTION:
Implement a function `binary_search(arr, x)` that performs a binary search on a sorted array `arr` to find the index of a target element `x`. The function should return the index of `x` if found, and -1 otherwise. The array `arr` is sorted in ascending order, and the function should use a while loop to iteratively divide the search space.
"""

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore the left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # If x found at mid index
        else:
            return mid

    # If we reach here, then the element was not present
    return -1