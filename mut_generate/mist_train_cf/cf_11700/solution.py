"""
QUESTION:
Implement a function `merge_sort_descending(arr)` that sorts an array of strings in alphabetical order in descending direction with a time complexity of O(n log n). The input array `arr` contains strings, and the function should return the sorted array.
"""

def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort_descending(left_half)
    right_half = merge_sort_descending(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:  # Compare strings in descending order
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result