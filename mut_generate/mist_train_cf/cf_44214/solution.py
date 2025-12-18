"""
QUESTION:
Implement a function named `quicksort` that sorts a list of integers in descending order using the quicksort algorithm. The function should take one argument, `arr`, which is the list of integers to be sorted. The function should return the sorted list. The implementation should be able to handle lists with duplicate elements and empty lists.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return quicksort(left) + middle + quicksort(right)