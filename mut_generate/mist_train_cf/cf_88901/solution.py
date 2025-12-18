"""
QUESTION:
Implement the `recursive_binary_search` function that takes a sorted descending list `arr`, a target element `target`, and a range defined by `start` and `end` indices, and returns the index of the second occurrence of the target element in the list. The function should use a recursive binary search algorithm and handle duplicates in the list. If the second occurrence does not exist, return -1. The function should be efficient and handle edge cases.
"""

def recursive_binary_search(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        left_occurrence = recursive_binary_search(arr, target, start, mid - 1)
        right_occurrence = recursive_binary_search(arr, target, mid + 1, end)

        if left_occurrence == -1 and right_occurrence == -1:
            return -1
        elif left_occurrence == -1:
            return right_occurrence
        else:
            return left_occurrence
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, mid + 1, end)
    else:
        return recursive_binary_search(arr, target, start, mid - 1)