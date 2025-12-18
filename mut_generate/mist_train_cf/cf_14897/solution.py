"""
QUESTION:
Write a function named `is_sorted_asc` that checks if a given list of integers is sorted in ascending order without using any built-in sorting functions. The function should take one argument, a list of integers, and return a boolean value indicating whether the list is sorted in ascending order. The function should work correctly for lists of any length, including empty lists and lists with a single element.
"""

def is_sorted_asc(arr):
    n = len(arr)
    if n <= 1:
        return True

    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False

    return True