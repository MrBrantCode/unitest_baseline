"""
QUESTION:
Implement the quick_sort function, which takes an array of integers as input and returns a sorted array in ascending order using the quick sort algorithm. The function should be able to handle arrays containing both positive and negative numbers, and it should place duplicate numbers next to each other in the sorted array. The implementation should not use any built-in sorting functions or libraries.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)