"""
QUESTION:
Implement a function called `quicksort_descending` that sorts an array of integers in descending order using the quicksort algorithm with a time complexity of O(n log n) without using recursion or additional data structures. The function should handle arrays containing duplicate elements.
"""

def quicksort_descending(arr):
    stack = [(0, len(arr) - 1)]  # Initialize stack with the range of indices to be sorted

    while stack:
        start, end = stack.pop()  # Get the next subarray to be sorted

        if start >= end:
            continue

        pivot = arr[end]  # Choose the last element as the pivot
        i = start - 1

        for j in range(start, end):
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        i += 1
        arr[i], arr[end] = arr[end], arr[i]

        # Push the left and right subarrays to the stack
        stack.append((start, i - 1))
        stack.append((i + 1, end))

    return arr