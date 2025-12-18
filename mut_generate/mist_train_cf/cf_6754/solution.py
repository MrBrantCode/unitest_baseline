"""
QUESTION:
Write a function called `merge_sort` that sorts a list of integers in descending order using a recursive merge sort algorithm. The function should not use any built-in sorting functions or libraries. It should take a list of integers as input and return the sorted list.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left_half, right_half):
    merged = []
    i, j = 0, 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] > right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    while i < len(left_half):
        merged.append(left_half[i])
        i += 1

    while j < len(right_half):
        merged.append(right_half[j])
        j += 1

    return merged