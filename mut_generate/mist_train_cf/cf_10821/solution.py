"""
QUESTION:
Implement a function named merge_sort that takes a list of integers as input and returns the sorted list. The time complexity of this function should be O(n log n). The input list can contain duplicate elements and the function should be stable, meaning that the order of equal elements should be preserved.
"""

def merge_sort(arr):
    """
    Sorts a list of integers using the merge sort algorithm.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A sorted list of integers.

    Time Complexity:
        O(n log n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged