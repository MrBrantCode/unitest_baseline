"""
QUESTION:
Implement a function `quicksort(arr)` that sorts an array of integers in ascending order using the Quicksort algorithm. The array can have arbitrary length and is not pre-sorted. The function should return the sorted array.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)