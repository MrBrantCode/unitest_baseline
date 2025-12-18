"""
QUESTION:
Implement a function `quick_sort(arr)` that sorts an input list of integers in ascending order using the quicksort algorithm without using built-in Python sorting functions. Optimize the code for performance as much as possible. The function should take a list of integers as input and return the sorted list.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = sorted([arr[0], arr[len(arr) // 2], arr[-1]])[1]
    return quick_sort([x for x in arr if x < pivot]) + [x for x in arr if x == pivot] + quick_sort([x for x in arr if x > pivot])