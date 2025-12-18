"""
QUESTION:
Implement a function named `binary_insertion_sort` that sorts a list of integers in non-decreasing order using the insertion sort algorithm with binary search to find the proper position for insertion. The function should take a list of integers as input and return the sorted list.
"""

import bisect

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        bisect.insort(arr, arr.pop(i), 0, i)
    return arr