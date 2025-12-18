"""
QUESTION:
Implement a stable sorting algorithm, specifically the merge sort algorithm, in Python, in a function named `merge_sort`, that takes an input list and returns a sorted list while preserving the initial order of equivalent entities. The input list may contain diverse data categories such as numerical, alphabetical, and chronological structures.
"""

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left_half = merge_sort(input_list[:mid])
    right_half = merge_sort(input_list[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If we've exhausted one list, append all remaining items from the other
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged