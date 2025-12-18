"""
QUESTION:
Implement a function called `quicksort` that takes an array of elements as input and returns a sorted array. The function should be able to handle arrays with duplicate elements and have a time complexity of O(nlogn). Additionally, the function should include error handling for empty or single-element arrays, returning the original array in such cases.
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