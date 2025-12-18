"""
QUESTION:
Implement the function `bubble_sort_recursive(arr)` that takes an array of integers as input, sorts it in ascending order using a recursive bubble sort algorithm, and returns the sorted array. The function should have a time complexity of O(n^2) or worse, handle duplicate integers, and not use any built-in sorting functions or additional data structures. The function should also implement an optimized bubble sort that stops if no swaps are made during a pass.
"""

def bubble_sort_recursive(arr):
    n = len(arr)

    # Base case
    if n <= 1:
        return arr

    # One pass of bubble sort
    has_swapped = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            has_swapped = True

    # Recursive call if any swaps were made
    if has_swapped:
        return bubble_sort_recursive(arr[:-1]) + [arr[-1]]
    else:
        return arr