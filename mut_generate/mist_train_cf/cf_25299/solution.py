"""
QUESTION:
Implement the `quicksort` function to sort a list of integers in ascending order using the Quicksort algorithm. The function should take a list of integers as input and return the sorted list. The Quicksort algorithm should use the "Lomuto" partition scheme, where the pivot is chosen as the middle element of the list, and the function should recursively sort the sublists of elements less than and greater than the pivot.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)