"""
QUESTION:
Implement a function called `quickSort` that sorts an array of integers in-place using the quick sort algorithm. The function should take an array as input and return the sorted array. The array may contain duplicate elements.
"""

def entance(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return entance(left) + middle + entance(right)