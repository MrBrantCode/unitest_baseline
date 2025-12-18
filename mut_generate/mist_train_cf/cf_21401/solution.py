"""
QUESTION:
Write a function named 'median' that calculates the median of an array of integers. The array will always have at least one element and may contain duplicate elements. The function should not use any loops, recursion, or built-in sorting functions.
"""

def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def median(array):
    sorted_array = quicksort(array)
    length = len(sorted_array)
    if length % 2 == 1:
        return sorted_array[length // 2]
    else:
        return (sorted_array[length // 2 - 1] + sorted_array[length // 2]) / 2