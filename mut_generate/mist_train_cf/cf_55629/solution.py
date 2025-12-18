"""
QUESTION:
Write a function `binary_search(arr, low, high, x)` that uses a recursive binary search technique to locate an element `x` within a chronologically ordered array. The function should take an array `arr`, starting index `low`, ending index `high`, and a searching element `x` as parameters, and return the index of `x` if found, or -1 if `x` is not in the array. The function should also handle the edge case where the element is not found in the array.
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