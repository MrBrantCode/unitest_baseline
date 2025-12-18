"""
QUESTION:
Implement a function `binary_search` that performs binary search on a pre-sorted numerical array to find a specific element. The function should take four parameters: a pre-sorted array `arr`, the starting index `low`, the ending index `high`, and the target element `x`. The function should return the index of the target element if found, and -1 otherwise.
"""

def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1