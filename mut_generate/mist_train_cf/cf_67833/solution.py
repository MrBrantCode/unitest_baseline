"""
QUESTION:
Implement a function named `binary_search` that takes a sorted array `arr`, a low index `low`, a high index `high`, and a target value `x` as input, and returns the index of `x` in `arr` if it exists, or -1 if it does not exist. The array is sorted in ascending order and the function should use the Binary Search algorithm to find the target value.
"""

def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1