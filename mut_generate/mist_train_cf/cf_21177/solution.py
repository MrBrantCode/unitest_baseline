"""
QUESTION:
Implement the function `merge_sort` that takes a list of at least 1,000,000 elements as input and returns the sorted list in ascending order. The function must have a time complexity of O(n log n) or better and utilize a divide and conquer approach.
"""

def merge_sort(arr):
    """
    Sorts a list of elements in ascending order using the Merge Sort algorithm.

    Args:
        arr (list): The input list to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    # Base case: If the array has one or zero elements, it is already sorted.
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves.
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves.
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.

    Returns:
        list: The merged sorted list.
    """
    merged = []
    left_index = 0
    right_index = 0

    # Compare elements from both lists and append the smaller one to the merged list.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are remaining elements in either list, append them to the merged list.
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged