"""
QUESTION:
Implement a function named `quicksort` that sorts an array of alphanumeric characters in lexicographical order using the Quick Sort algorithm. The function should work recursively and handle strings of any length.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)