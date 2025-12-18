"""
QUESTION:
Implement the quicksort function to recursively sort a list of integers. The function should take a list of integers as input, choose a pivot element, partition the list into sublists of smaller and greater elements, and recursively apply the function to the sublists until each sublist has only one element. The function should then concatenate the sorted sublists and return the final sorted list.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)