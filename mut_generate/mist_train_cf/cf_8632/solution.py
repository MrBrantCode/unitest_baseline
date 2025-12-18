"""
QUESTION:
Implement a function mergeSort(array) that sorts an input array of integers in ascending order. The function should have a time complexity of O(n log n), not O(n^2), and should not use any built-in sorting functions or data structures. The function should be stable, adaptive, and able to handle large input arrays with a size up to 10^6, containing integers ranging from -1000 to 1000, with possible duplicates.
"""

def merge_sort(array):
    """
    Sorts an input array of integers in ascending order using the merge sort algorithm.

    Args:
        array (list): Input array of integers.

    Returns:
        list: Sorted array of integers.
    """
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.

    Args:
        left (list): First sorted array.
        right (list): Second sorted array.

    Returns:
        list: Merged sorted array.
    """
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result