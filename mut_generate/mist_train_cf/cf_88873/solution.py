"""
QUESTION:
Implement a function called `merge_sort` that takes an array of tuples as input, where each tuple has two elements: an integer and a character. The function should sort the array in ascending order based on the integer values, while preserving the relative order of equal elements (based on the character values). The function should have a time complexity of O(n log n) and use a constant amount of additional memory. The function should be stable, meaning that the relative order of equal elements should be preserved.
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

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result