"""
QUESTION:
Implement a function named `bubble_sort_recursive` that recursively sorts a list of integers in increasing order without using any built-in sorting method, additional data structures, or modifying the original list. The function should have a time complexity of O(n^2) and a space complexity of O(1), and it should take the list and its length as inputs.
"""

def bubble_sort_recursive(arr, n):
    if n == 1:
        return arr
    
    # Perform a single pass of bubble sort
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # Recursive call with n-1 elements
    bubble_sort_recursive(arr, n - 1)