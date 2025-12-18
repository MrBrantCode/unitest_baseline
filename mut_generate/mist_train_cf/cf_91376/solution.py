"""
QUESTION:
Implement a function called `quicksort` that sorts a given array using the quicksort algorithm recursively without using any built-in sorting functions or libraries. The function should take an array as input and return the sorted array.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)