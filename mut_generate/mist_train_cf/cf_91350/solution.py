"""
QUESTION:
Create a function named `bubble_sort` that takes an array of integers as input and returns the sorted array in ascending order without using the built-in `sort()` function or recursion. Note that while the implementation cannot use explicit loops or recursion, solutions that use loops or recursion implicitly are acceptable.
"""

def bubble_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True

    return arr