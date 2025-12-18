"""
QUESTION:
Implement a function `quick_sort(arr)` that takes a 1D array of floating-point numbers and sorts it using the Quick Sort algorithm. The input array should be a flattened version of a 3D numeric matrix of size 2x2x5, consisting of 20 floating-point values. The function should return the sorted array.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)