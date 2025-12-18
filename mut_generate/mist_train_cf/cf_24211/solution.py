"""
QUESTION:
Implement a function merge_sort that takes an array of n integers as input and returns the sorted array in ascending order. The function should have a time complexity of O(n log n).
"""

def merge_sort(arr):
    """
    Sorts an array of integers in ascending order using the merge sort algorithm.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A sorted list of integers in ascending order.
    """
    # If the array has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index of the array
    mid = len(arr) // 2

    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted left and right halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left (list): A sorted list of integers.
        right (list): A sorted list of integers.

    Returns:
        list: A sorted list of integers.
    """
    merged = []
    left_index = 0
    right_index = 0

    # Merge smaller elements first
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are remaining elements in either the left or right list, append them to the merged list
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged