"""
QUESTION:
Implement a function `recursive_selection_sort(arr, start)` that recursively sorts a list of unique numbers in increasing order without using any built-in sorting methods or additional data structures. The function should have a time complexity of O(n^2) and a space complexity of O(1), and it should sort the list in-place without modifying the original list's structure. The function takes a list `arr` and an integer `start` as parameters, where `start` represents the starting index of the unsorted part of the list.
"""

def recursive_selection_sort(arr, start):
    if start >= len(arr) - 1:
        return
    
    # Find the minimum element in the unsorted part
    min_index = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    
    # Swap the minimum element with the first element in the unsorted part
    arr[start], arr[min_index] = arr[min_index], arr[start]
    
    # Recursively sort the remaining list
    recursive_selection_sort(arr, start + 1)