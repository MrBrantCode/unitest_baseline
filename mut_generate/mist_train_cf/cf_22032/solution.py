"""
QUESTION:
Implement a function named `binary_search_with_index` that performs a binary search on a sorted list of integers in ascending order. The function should return the target element and its index, where the index corresponds to the first occurrence of the element in the list. If the target element is not found, return `(None, -1)`. The function should take two parameters: `arr` (the sorted list of integers) and `target` (the target integer to be searched).
"""

def binary_search_with_index(arr, target):
    left = 0
    right = len(arr) - 1
    index = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            index = mid
            right = mid - 1  # look for the first occurrence on the left side
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if index != -1:
        return arr[index], index
    else:
        return None, -1