"""
QUESTION:
Implement a function called `insertion_sort` that sorts an array of integers in ascending order using the insertion sort algorithm without using loops or recursion. The function should take an array as input and return the sorted array. Note that the input array is expected to contain only integers, and the function should handle arrays of any length, including empty arrays.
"""

def insertion_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Recursively sort the first n-1 elements
    sorted_arr = insertion_sort(arr[:-1])
    
    # Find the correct position to insert the last element
    pos = len(sorted_arr)
    while pos > 0 and sorted_arr[pos-1] > arr[-1]:
        pos -= 1
    
    # Insert the last element at the correct position
    sorted_arr.insert(pos, arr[-1])
    
    return sorted_arr