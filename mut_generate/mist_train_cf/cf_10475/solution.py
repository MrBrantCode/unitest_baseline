"""
QUESTION:
Implement a function named `quicksort` that sorts an array in ascending order using the quicksort algorithm. The function must be implemented recursively and cannot use any built-in sorting functions or libraries. The input is an array of integers, and the output is the sorted array.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)