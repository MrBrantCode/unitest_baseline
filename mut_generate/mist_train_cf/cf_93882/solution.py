"""
QUESTION:
Implement a function `quicksort(arr)` that takes an array of integers as input and returns a sorted array. The function should be able to handle arrays with duplicate elements, be able to handle arrays with less than 2 elements, and have an average time complexity of O(nlogn).
"""

def quicksort(arr):
    # Error handling for empty or single-element arrays
    if len(arr) < 2:
        return arr

    # Selecting a pivot element
    pivot = arr[len(arr)//2]
    
    # Partitioning the array
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    # Recursive sorting of sub-arrays
    return quicksort(less) + equal + quicksort(greater)