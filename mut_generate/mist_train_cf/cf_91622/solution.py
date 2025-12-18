"""
QUESTION:
Implement a function named `quicksort` that sorts an array of integers in ascending order using the quicksort algorithm. The function should take a list of integers as input and return the sorted list. The function should be able to handle arrays of any size, including empty arrays and arrays with duplicate elements.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)