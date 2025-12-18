"""
QUESTION:
Implement a function named `quicksort` that takes a list of integers as input and returns a sorted list using the quicksort algorithm. The function should be able to handle lists of any size, including empty lists and lists with duplicate values. The input list should only contain integers.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)