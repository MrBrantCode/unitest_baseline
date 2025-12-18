"""
QUESTION:
Implement a function named `binary_search` that takes a sorted list `arr`, a target element `target`, and two indices `start` and `end` as parameters. The function should return the index of the target element if it is present in the list, or -1 if it is not present. The function must have a time complexity of O(log n) and be able to handle both even and odd-length lists, lists with duplicate elements, and empty lists. The function should not use any built-in functions or libraries for binary search.
"""

def binary_search(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr, target, start, mid - 1)