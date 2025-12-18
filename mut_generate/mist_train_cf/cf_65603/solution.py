"""
QUESTION:
Create a function `binary_search` that takes a sorted list of complex numbers, a target complex number, and the start and end indices as input. The function should return the index of the target complex number in the list if it exists, otherwise return -1. The complex numbers in the list are sorted in ascending order based on their magnitude. Assume that the list of complex numbers is already loaded and sorted. 

Note: The magnitude of a complex number is calculated as the square root of the sum of the squares of its real and imaginary parts. The list of complex numbers should be sorted based on this magnitude.
"""

import cmath

def binary_search(array, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif cmath.polar(array[mid])[0] > cmath.polar(target)[0]:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)