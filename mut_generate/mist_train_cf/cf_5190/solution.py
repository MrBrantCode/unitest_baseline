"""
QUESTION:
Implement a function named `quicksort` that takes an array of elements as input and returns the sorted array. The function should handle duplicate elements in the input array.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    equal = [x for x in arr if x == pivot]
    lesser = [x for x in arr if x < pivot]
    greater = [x for x in arr if x > pivot]

    return quicksort(lesser) + equal + quicksort(greater)