"""
QUESTION:
Write a function named `find_first_last_index` that takes a sorted array `arr` in descending order and a target element `target` as input and returns a list containing the first and last index of the target element in the array. If the target element is not found, return [-1, -1].
"""

def find_first_last_index(arr, target):
    first_index = -1
    last_index = -1

    start = 0
    end = len(arr) - 1

    # Find first occurrence
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            first_index = mid
            end = mid - 1
        elif arr[mid] > target:
            start = mid + 1
        else:
            end = mid - 1

    if first_index == -1:
        return [-1, -1]

    start = 0
    end = len(arr) - 1

    # Find last occurrence
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            last_index = mid
            start = mid + 1
        elif arr[mid] > target:
            start = mid + 1
        else:
            end = mid - 1

    return [first_index, last_index]