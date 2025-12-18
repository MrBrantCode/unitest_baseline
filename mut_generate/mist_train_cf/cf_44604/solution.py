"""
QUESTION:
Implement a function `binary_search(arr, low, high, x)` that uses a binary search strategy to find the position of a distinct element `x` within a sequentially sorted array `arr` in chronological order, where `low` and `high` represent the range of the array to be searched. The function should return the index of `x` if found, and -1 otherwise. Assume the input array is sorted in ascending order.
"""

# Function for Binary Search
def entrance(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return entrance(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return entrance(arr, mid + 1, high, x)
 
    else:
        # Element is not present in array
        return -1