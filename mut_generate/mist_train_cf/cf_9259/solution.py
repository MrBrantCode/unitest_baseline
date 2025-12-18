"""
QUESTION:
Write a function named `merge_sort` to sort a list of strings by length in descending order. If two strings have the same length, they should be sorted lexicographically. The time complexity of the solution should be O(nlogn), and built-in sorting functions should not be used.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if len(left[i]) > len(right[j]):
            merged.append(left[i])
            i += 1
        elif len(left[i]) < len(right[j]):
            merged.append(right[j])
            j += 1
        else:
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged