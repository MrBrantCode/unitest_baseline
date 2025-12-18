"""
QUESTION:
Implement a function named "quicksort" that takes an array of elements as input and returns the sorted array. The function should be efficient, with a time complexity of O(n log n), and should be able to handle arrays of varying sizes.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)