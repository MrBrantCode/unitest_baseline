"""
QUESTION:
Create a function named `sort_array` that takes an array of numbers as input and returns the array sorted in descending order. The function should implement a sorting algorithm such as quicksort or mergesort instead of using built-in sorting functions. The input array may contain duplicate numbers, negative numbers, floating-point numbers, and up to 100,000 elements.
"""

def sort_array(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return sort_array(left) + middle + sort_array(right)