"""
QUESTION:
Implement a function `quickSort(arr)` that takes a list of integers as input and returns a new list containing the same integers in ascending order. The function should use the QuickSort algorithm, utilizing a divide-and-conquer strategy with partitioning, recursion, and combining. The function should have a base case for lists of length 1 or less, and should recursively sort sub-lists of elements less than and greater than a chosen pivot element.
"""

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quickSort(left) + middle + quickSort(right)