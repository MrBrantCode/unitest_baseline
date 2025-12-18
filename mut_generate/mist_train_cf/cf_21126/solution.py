"""
QUESTION:
Implement a Python function called `binary_search_first_occurrence` that takes a sorted array of integers `arr`, a target element `target`, and a starting index `low` (defaulting to 0) as input. The function should return the index of the first occurrence of the target element in the array, or -1 if the target element is not found. Assume the array is sorted in ascending order and contains no duplicates.
"""

def binary_search_first_occurrence(arr, target, low=0):
    high = len(arr) - 1

    # Check if the array is empty
    if len(arr) == 0:
        return -1

    # Check if there's only one element in the array
    if len(arr) == 1:
        return 0 if arr[0] == target else -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            # Check if it's the first occurrence of the target element
            if mid > 0 and arr[mid - 1] == target:
                high = mid - 1
            else:
                return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1