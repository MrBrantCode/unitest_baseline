"""
QUESTION:
Implement a function `quicksort_descending(arr)` to sort the given array `arr` in descending order. The array may contain duplicate elements. The function should have a time complexity of O(n log n) and should not use any additional data structures beyond a stack or recursion.
"""

def quicksort_descending(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        start, end = stack.pop()

        if start >= end:
            continue

        pivot = arr[end]
        i = start - 1

        for j in range(start, end):
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        i += 1
        arr[i], arr[end] = arr[end], arr[i]

        stack.append((start, i - 1))
        stack.append((i + 1, end))

    return arr