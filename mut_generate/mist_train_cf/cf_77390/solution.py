"""
QUESTION:
Design a sorting function, `merge_sort`, that can efficiently sort a large sequence of numeric integer values. The function should achieve a good space-time trade-off, have optimal computational complexity in best, average, and worst-case scenarios, and be amenable to optimization. Assume the input is a list of integers.
"""

def merge_sort(arr):
    """
    Sorts a list of integers using the Merge Sort algorithm.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A sorted list of integers.
    """
    # If the array has 1 or fewer elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point of the array
    mid = len(arr) // 2

    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively call merge_sort on the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted lists into one sorted list.

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
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are remaining elements in the left or right lists, append them to the merged list
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged