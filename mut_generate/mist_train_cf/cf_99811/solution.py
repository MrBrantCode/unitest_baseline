"""
QUESTION:
Implement the `quicksort` function that sorts an array of integers in ascending order. The function should take a list of integers as input and return a sorted list. The function should be able to handle arrays of arbitrary length and should not assume the input array is pre-sorted.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)