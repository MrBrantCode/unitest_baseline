"""
QUESTION:
Implement the MergeSort algorithm in a function named `merge_sort`. The function should take a list of elements as input and return a sorted list. The algorithm should use a divide-and-conquer approach, recursively dividing the input list into smaller sublists until each sublist contains only one element, and then merging the sublists to produce the sorted output. The function should not use any built-in sorting functions or methods.
"""

def merge_sort(arr):
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
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged