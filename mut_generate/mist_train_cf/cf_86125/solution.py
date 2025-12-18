"""
QUESTION:
Implement a function named `quicksort` that sorts the elements of a given array in ascending order. The function should take an array of integers as input and return a new array containing the same elements in sorted order.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)