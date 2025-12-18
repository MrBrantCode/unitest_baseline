"""
QUESTION:
Implement a function named binary_search that takes a sorted list of integers and a key value as input, and returns the position of the key value in the list with a time complexity of O(log n). If the key value is not found, return an error message. The list is sorted in ascending order.
"""

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return f"The key value '{key}' is found at position {mid + 1}."
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return f"The key value '{key}' is not present in the list."