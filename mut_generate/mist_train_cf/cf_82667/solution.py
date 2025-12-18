"""
QUESTION:
Create a function `quick_sort(arr)` that recursively sorts an array of numeric elements in descending order without using the built-in sort function. The function should take an array `arr` as input, partition it around a pivot element, recursively sort the sub-arrays, and return the sorted array. The function should handle arrays with any number of elements, including empty arrays and arrays with duplicate elements.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return quick_sort(left) + middle + quick_sort(right)