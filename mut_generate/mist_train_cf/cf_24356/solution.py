"""
QUESTION:
Implement a function `sort_integers` that sorts n integers in ascending order using a divide-and-conquer algorithm. The function should take a list of integers as input and return a sorted list of integers. The integers can be positive, negative, or zero, and there are no duplicate integers in the list. The function should have a time complexity of O(n log n).
"""

def sort_integers(nums):
    """
    Sorts a list of integers in ascending order using the merge sort algorithm.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A sorted list of integers in ascending order.
    """
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_half = sort_integers(nums[:mid])
    right_half = sort_integers(nums[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged