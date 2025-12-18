"""
QUESTION:
Implement a binary search function named `binary_search` that takes a list `arr` and a target element `target` as input. The function should return the index of the first occurrence of the target element if found, or -1 if not found. The list may contain duplicate elements and can be sorted in either ascending or descending order within sections. The function should have a time complexity of O(log n). If the input list is not sorted, the function should raise an exception.
"""

def binary_search(arr, target):
    if not is_sorted(arr):
        raise Exception("Input list is not sorted")

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return find_first_occurrence(arr, target, low, mid)
        elif arr[mid] < target:
            if arr[low] <= arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if arr[low] <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return -1


def find_first_occurrence(arr, target, low, high):
    while low < high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))