"""
QUESTION:
Implement a recursive Quick Sort function named 'quicksort' that takes an array of integers as input, has a time complexity of O(nlogn) in all cases, and does not use any built-in sorting functions or libraries. The function should correctly sort the array by recursively partitioning it around a pivot element and combining the sorted subarrays. Ensure that the pivot element is correctly placed in its final sorted position to avoid infinite loops.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)