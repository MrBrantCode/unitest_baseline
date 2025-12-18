"""
QUESTION:
Write a recursive function named `binary_search` that searches for a value in a sorted list. The function should take four parameters: a list of integers `arr`, the lowest index `low`, the highest index `high`, and the target value `x`. Return the index of the target value if found, otherwise return -1.
"""

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1