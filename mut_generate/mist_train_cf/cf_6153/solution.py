"""
QUESTION:
Implement a function `merge_sort()` that takes a list of strings as input, sorts them in descending order based on the length of each string, and maintains the original order for strings of the same length. The function should have a time complexity of O(n log n) and should not use any built-in sorting functions or libraries.
"""

def merge_sort(lst):
    """
    Sorts a list of strings in descending order based on the length of each string, 
    maintaining the original order for strings of the same length.

    Args:
        lst (list): A list of strings.

    Returns:
        list: A sorted list of strings.
    """
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.

    Returns:
        list: A merged sorted list.
    """
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if len(left[left_index]) >= len(right[right_index]):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result