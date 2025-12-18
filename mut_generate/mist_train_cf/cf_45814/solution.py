"""
QUESTION:
Implement a function named `quicksort` that takes an array of elements of any primitive type as input and sorts it in-place using the QuickSort algorithm. The function should be capable of handling edge cases where the array is already sorted or reverse sorted, and it should work with arrays of integers, characters, strings, etc. Analyze the time and space complexity of the function.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)