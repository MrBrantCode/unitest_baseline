"""
QUESTION:
Write a function `quicksort` that implements the quicksort algorithm to sort an array of integers in ascending order. The function should take an array as input and return the sorted array. It should include the necessary steps involved in partitioning the array and choosing the pivot element. The function should handle edge cases such as an empty array or an array with only one element.
"""

def quicksort(arr):
    # Base case: empty or single element array
    if len(arr) <= 1:
        return arr
    
    # Choose pivot element (here, we choose the first element)
    pivot = arr[0]
    
    # Partition the array
    smaller = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    
    # Recursively sort the smaller and greater sub-arrays
    return quicksort(smaller) + [pivot] + quicksort(greater)