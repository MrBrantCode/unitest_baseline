"""
QUESTION:
Implement the quick_sort function, which sorts a given list of integers in ascending order using the quick sort algorithm. The function should handle lists containing both positive and negative integers, as well as duplicate values, without using any built-in sorting functions.
"""

def quick_sort(arr):
    if len(arr) <= 1: 
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)