"""
QUESTION:
Design a function named `binary_search` that takes a sorted array `arr` and a target integer `target` as input, and returns the index of the target in the array if found. If the target is not found, the function should return 'Not Found'. The function should work with both positive and negative integers, as well as zero, and assume that the input array is sorted in ascending order.
"""

def binary_search(arr, target):
    left = 0 
    right = len(arr) - 1 

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid   # Element is found, so return the index.
        elif arr[mid] < target:  
            left = mid + 1 # Element is not on the left side, so consider right side.
        else:
            right = mid - 1 # Element is not on the right side, so consider left side.

    # If the element is not found, return 'Not Found'.
    return 'Not Found'