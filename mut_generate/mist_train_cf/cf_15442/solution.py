"""
QUESTION:
Implement a function `merge_sort` to sort a list of strings in descending order of their lengths while minimizing space complexity. The function should use a stable sorting algorithm and return the sorted list. The input list contains only strings, and the output should be a list of the same strings sorted by their lengths in descending order. The sorting algorithm should maintain the original order of strings with equal lengths.
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
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if len(left[i]) >= len(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result