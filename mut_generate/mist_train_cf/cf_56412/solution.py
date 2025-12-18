"""
QUESTION:
Implement a function named `optimized_sort` that takes a list of integers, floats, and/or negative numbers as input and returns the sorted list in ascending order without using the built-in `sort()` or `sorted()` functions. The function should handle lists of varying lengths, including empty lists, and optimize the sorting process for nearly sorted lists.
"""

def optimized_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr