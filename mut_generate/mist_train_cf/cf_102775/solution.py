"""
QUESTION:
Implement a function named `binary_search` that performs a binary search on a sorted array to find the index of a given target element. The function should take the sorted array, the low and high indices of the search range, and the target element as arguments, and return the index of the target element if found, or -1 if not found. The function should have a runtime complexity of O(log n).
"""

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (low + high) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    # Element is not present in array
    return -1