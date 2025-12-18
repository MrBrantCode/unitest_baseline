"""
QUESTION:
Create a function named `sort_and_remove_duplicates` that takes a list of numbers as input, removes any duplicate numbers, and returns the list sorted in ascending order without using built-in sorting functions or libraries. The function should implement a recursive sorting algorithm such as quicksort or mergesort.
"""

def sort_and_remove_duplicates(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return sort_and_remove_duplicates(left) + middle[:1] + sort_and_remove_duplicates(right)