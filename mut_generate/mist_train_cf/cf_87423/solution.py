"""
QUESTION:
Write a recursive function `merge_sort` that sorts a list of strings alphabetically in ascending order with a time complexity of O(n log n), ignoring case sensitivity and without using the built-in sorting function or any sorting algorithm with lower time complexity. The function should handle lists containing any number of strings.
"""

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index].lower() < right[right_index].lower():
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged