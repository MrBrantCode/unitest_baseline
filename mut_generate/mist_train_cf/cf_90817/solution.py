"""
QUESTION:
Write a function `merge_sort` that takes a list of strings as input and returns the list sorted by string length in descending order. In case of a tie, sort the strings lexicographically. The function should have a time complexity of O(nlogn) and should not use any built-in sorting functions.
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