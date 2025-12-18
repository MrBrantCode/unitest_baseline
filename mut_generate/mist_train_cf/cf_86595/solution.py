"""
QUESTION:
Create a function named `sort_array` that takes one argument `arr`, an array of integers, and returns the array sorted in descending order. The function should implement a sorting algorithm to arrange the elements of the array from largest to smallest. The input array can contain duplicate values and may be unsorted.
"""

def sort_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr