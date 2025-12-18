"""
QUESTION:
Implement a function named `sort_descending` that sorts an array of numbers in descending order without using built-in sorting functions. The function should be able to handle arrays with duplicate numbers, negative numbers, and floating-point numbers. The function should take one parameter, an array of numbers, and return the sorted array.
"""

def sort_descending(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return sort_descending(left) + middle + sort_descending(right)