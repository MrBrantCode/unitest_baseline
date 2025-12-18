"""
QUESTION:
Implement a function `binary_search` that takes a sorted array of discrete integers and a target value as input, and returns the index of the target value in the array if found, or -1 if not found. The array is pre-allocated and contains no duplicates.
"""

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high: 
        mid = (high + low) // 2

        # If x greater than number in the middle of the array, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller than the middle number ignore the right half
        elif arr[mid] > x:
            high = mid - 1

        # x is found, return the index
        else:
            return mid

    # x is not present in the array
    return -1