"""
QUESTION:
Implement a function called `merge_sort` to sort a list of integers in ascending order using the MergeSort algorithm. The function should take a list of integers as input and return the sorted list. The implementation should follow the divide-and-conquer approach, dividing the input list into two halves, recursively sorting each half, and then merging the sorted halves back together.
"""

def merge_sort(arr):
    """
    Sorts a list of integers in ascending order using the MergeSort algorithm.

    Args:
    arr (list): A list of integers to be sorted.

    Returns:
    list: The sorted list of integers.
    """

    # Base case: If the list has 1 or 0 elements, it is already sorted.
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves.
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves back together.
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

    # Merge smaller elements first.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are remaining elements in either half, append them to the merged list.
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged