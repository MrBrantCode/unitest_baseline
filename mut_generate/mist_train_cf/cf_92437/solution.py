"""
QUESTION:
Write a function named `binary_search(vector, x)` that performs a binary search on a sorted vector to find a given element `x` with a time complexity of O(log n), where n is the number of elements in the vector. The function should return the index of `x` if found, otherwise return -1. The vector is sorted in ascending order.
"""

def binary_search(vector, x):
    low = 0
    high = len(vector) - 1

    while low <= high:
        mid = (low + high) // 2

        if vector[mid] == x:
            return mid
        elif vector[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found