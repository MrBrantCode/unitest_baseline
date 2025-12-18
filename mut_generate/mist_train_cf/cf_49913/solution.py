"""
QUESTION:
Implement a function called `binary_search` that takes a sorted array of integers and a target number as input, and returns the index of the target number if it exists in the array. If the target number is not found, return -1. The function should stop searching as soon as the number is found. Assume the input array is sorted in ascending order.
"""

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # x is present at mid, so return index
        else:
            return mid

    # If x is not present in array 
    return -1