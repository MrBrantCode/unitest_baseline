"""
QUESTION:
Implement a function named `quicksort` that takes an array of integers as input and returns the sorted array in ascending order using the Quicksort algorithm. The function should not use any built-in sorting methods and should be able to handle lists with duplicate values. The function should recursively sort the array by selecting a pivot element, partitioning the array into two sub-arrays (elements less than or equal to the pivot and elements greater than the pivot), and then sorting the sub-arrays.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)