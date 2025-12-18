"""
QUESTION:
Implement a function called `binary_search` that takes a sorted list of unique integers, an integer to search for, and returns the index of the integer if found, or -1 if not found. The function should use a recursive binary search algorithm to achieve optimal efficiency.
"""

def binary_search(arr, low, high, x):
 
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
        # Element is not present in array
        return -1