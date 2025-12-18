"""
QUESTION:
Implement a function called `bubble_sort_recursive` that takes a list of positive integers as input and returns the sorted list in ascending order. The function must have a time complexity of O(n^2) and use a recursive approach without employing any built-in sorting functions or methods.
"""

def bubble_sort_recursive(arr):
    n = len(arr)
    
    # Base case: If the list is empty or has only one element, it is already sorted
    if n <= 1:
        return arr
    
    # Recursive case: Sort the list by swapping adjacent elements if they are in the wrong order
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    # Recursively sort the remaining list after excluding the last element
    return bubble_sort_recursive(arr[:-1]) + [arr[-1]]