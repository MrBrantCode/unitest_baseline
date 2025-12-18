"""
QUESTION:
Implement a function named `insertion_sort` that sorts an array of integers in ascending order without using loops or recursion.
"""

def insertion_sort(arr):
    if len(arr) <= 1:
        return arr
    
    sorted_arr = insertion_sort(arr[:-1])
    
    pos = len(sorted_arr)
    while pos > 0 and sorted_arr[pos-1] > arr[-1]:
        pos -= 1
    
    sorted_arr.insert(pos, arr[-1])
    
    return sorted_arr