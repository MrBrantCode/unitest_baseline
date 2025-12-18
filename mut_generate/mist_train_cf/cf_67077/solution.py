"""
QUESTION:
Implement a function `quicksort(arr)` that sorts an array of numbers (including integers and floating point numbers) in ascending order using the quick sort algorithm. The function should not use the built-in `sort()` function or any other sorting libraries. The input array can be of any size and may contain duplicate elements.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)