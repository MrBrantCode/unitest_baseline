"""
QUESTION:
Implement the `ternary_search` function that takes in a sorted list `arr` and a `key` to be searched, and returns the index of the `key` if it exists in the list, otherwise returns -1. The function should use the ternary search algorithm, dividing the list into three parts and determining in which part the element exists.
"""

def ternary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if key == arr[mid1]:
            return mid1
        elif key == arr[mid2]:
            return mid2

        if key < arr[mid1]:
            right = mid1 - 1
        elif key > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1