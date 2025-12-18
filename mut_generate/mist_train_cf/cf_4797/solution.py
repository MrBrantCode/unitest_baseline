"""
QUESTION:
Implement a stable sorting function named `merge_sort` to sort key-value pairs in ascending order based on their keys. The input is a list of records where keys are unique integers ranging from 1 to 1 million, and the output should be the sorted list of records. The function should not use any built-in sorting functions or libraries, have a space complexity of O(1), and a time complexity of O(n log n) where n is the number of records.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index][0] < right[right_index][0]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged