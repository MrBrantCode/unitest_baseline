"""
QUESTION:
Implement a function named `quick_sort` that takes an unsorted array of integers as input and returns the array sorted in ascending order using the quick sort algorithm. The array can contain both positive and negative numbers, and any duplicate numbers should be placed next to each other in the sorted array. Do not use any built-in sorting functions or libraries.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)