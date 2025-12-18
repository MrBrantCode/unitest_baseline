"""
QUESTION:
Implement a function named `binary_search_with_index` that performs a binary search on a sorted list of integers to find a target element. The function should return a tuple containing the target element and its index, where the index is of the first occurrence of the element if there are duplicates. If the target element is not found, the function should return `(None, -1)`. The function should take two parameters: a sorted list of integers `arr` and the target integer `target`.
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