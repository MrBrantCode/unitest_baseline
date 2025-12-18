"""
QUESTION:
Implement the function quicksort(arr) that takes an array of integers as input and returns the sorted array using the quicksort algorithm. The function should handle arrays of any size, including empty arrays, and should be able to sort arrays with duplicate elements.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)