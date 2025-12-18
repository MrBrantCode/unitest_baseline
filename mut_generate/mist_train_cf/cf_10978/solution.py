"""
QUESTION:
Implement the quicksort function to sort an array of integers in ascending order. The function should take a list of integers as input and return the sorted list. The function should use the quicksort algorithm, which recursively sorts the array by choosing a 'pivot' element and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)