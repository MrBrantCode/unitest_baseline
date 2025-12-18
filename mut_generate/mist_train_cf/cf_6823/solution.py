"""
QUESTION:
Implement a modified version of the quicksort algorithm, named `quicksort_iterative`, to sort a large, unsorted integer array in descending order. The algorithm should use the median of three pivot selection strategy and an iterative approach with a stack data structure to avoid recursive calls. The function should handle duplicate elements efficiently, ensuring that they appear in the correct order after sorting. The input array will contain at least 10^9 elements.
"""

def quicksort_iterative(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]

    while stack:
        start, end = stack.pop()

        if start < end:
            pivot_index = partition(arr, start, end)

            if pivot_index - 1 > start:
                stack.append((start, pivot_index - 1))

            if pivot_index + 1 < end:
                stack.append((pivot_index + 1, end))

    return arr[::-1]


def partition(arr, start, end):
    mid = (start + end) // 2

    if arr[start] > arr[mid]:
        arr[start], arr[mid] = arr[mid], arr[start]

    if arr[mid] > arr[end]:
        arr[mid], arr[end] = arr[end], arr[mid]

    if arr[start] > arr[mid]:
        arr[start], arr[mid] = arr[mid], arr[start]

    pivot = arr[mid]
    arr[mid], arr[end] = arr[end], arr[mid]
    i = start - 1

    for j in range(start, end):
        if arr[j] > pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1