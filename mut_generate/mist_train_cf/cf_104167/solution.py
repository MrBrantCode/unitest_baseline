"""
QUESTION:
Implement a function named `merge_sort` that sorts a list of numbers in ascending order using the Merge Sort algorithm. The function should take a list of numbers as input and return the sorted list. The input list may contain duplicate values, and the list can be of any length. The function should be able to handle lists with a length of 1 or less, and should be able to sort lists containing both positive and negative integers.
"""

def merge_sort(arr):
    """
    Sorts a list of numbers in ascending order using the Merge Sort algorithm.

    Args:
        arr (list): A list of numbers.

    Returns:
        list: The sorted list.
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