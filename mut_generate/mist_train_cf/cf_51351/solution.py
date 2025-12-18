"""
QUESTION:
Implement a function named quickSort that sorts a given list of integers using the QuickSort algorithm. The function should take a list of integers as input and return the sorted list. The implementation should include the partitioning phase, recursive looping, and should be able to handle the selection of a pivot element.
"""

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)