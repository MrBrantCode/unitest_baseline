"""
QUESTION:
Implement a binary search function named `binary_search` that takes a sorted list and a target element as input. The function should return the index of the target element if found, or -1 if not found. The function should be able to handle duplicate elements and return the index of the first occurrence. Additionally, it should be able to handle lists that contain both ascending and descending sections, and should raise an exception if the input list is not sorted. The function should have a time complexity of O(log n).
"""

def binary_search(arr, target):
    if not is_sorted(arr):
        raise Exception("Input list is not sorted")

    def find_first_occurrence(low, high):
        while low < high:
            mid = (low + high) // 2

            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid

        return low

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return find_first_occurrence(low, mid)
        elif arr[mid] < target:
            if arr[0] <= arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if arr[0] <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return -1


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))