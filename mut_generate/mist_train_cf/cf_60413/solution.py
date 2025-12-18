"""
QUESTION:
Implement a function named `quicksort` that sorts a given list of alphanumeric strings in ascending lexicographical order using the Quick sort algorithm. The function should take a list of strings as input and return the sorted list. The sorting should be based on standard string comparison rules.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)