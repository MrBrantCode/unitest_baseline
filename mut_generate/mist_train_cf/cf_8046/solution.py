"""
QUESTION:
Write a function named `swap_elements` that takes an array `arr` and two indices `i` and `j` as input. The function should swap the elements at indices `i` and `j` in the array without using a temporary variable. If `i` and `j` are out of bounds of the array or if they are the same, the function should return the array unchanged. The function should be able to handle arrays with any type of elements, including duplicates, negative values, floating-point numbers, strings, and objects.
"""

def swap_elements(arr, i, j):
    if i < 0 or i >= len(arr) or j < 0 or j >= len(arr):
        return arr  
    if i == j:
        return arr  
    arr[i] = arr[i] ^ arr[j]  
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]
    return arr