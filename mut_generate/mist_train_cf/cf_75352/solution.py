"""
QUESTION:
Implement a function called `recurse_search` that performs a recursive ternary search on a sorted 1D array. The function should take four parameters: a sorted 1D array `arr`, and three integers `left`, `right`, and `key`. It should return the index of the `key` in the array if found, and -1 otherwise. The function should prioritize the lowest index when multiple same-valued elements are found.
"""

def recurse_search(arr, left, right, key):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # If key is present at any mid
        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2

        # If key is not present, check in which region it is present
        # so as to adjust the search space
        if arr[mid1] > key:
            return recurse_search(arr, left, mid1 - 1, key)
        elif arr[mid2] < key:
            return recurse_search(arr, mid2 + 1, right, key)
        else:
            return recurse_search(arr, mid1 + 1, mid2 - 1, key)

    # Key is not present in array
    return -1