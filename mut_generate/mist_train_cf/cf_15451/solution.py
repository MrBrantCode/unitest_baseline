"""
QUESTION:
Create a function merge_sort(arr) that sorts the given array in decreasing order using only recursion and without using any built-in sorting functions or loops. The function should also remove any duplicate elements from the sorted array. The time complexity should be O(nlogn) and the space complexity should be O(logn).
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    result = []

    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(right[j])
            j += 1
        else:  # Handles duplicate elements
            result.append(left[i])
            i += 1
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result