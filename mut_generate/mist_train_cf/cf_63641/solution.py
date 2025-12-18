"""
QUESTION:
Create a function `sort_by_binary_len(arr)` that rearranges a set of non-negative integers based on their binary notation lengths in ascending order. If binary lengths are identical, sort them by their decimal values in ascending order. The function should perform well with large numbers in the array.
"""

def sort_by_binary_len(arr):
    """
    Rearrange an array of non-negative integers considering the lengths 
    of their binary notations. Sort the numbers by their decimal values 
    in case of binary length matches.

    """
    
    sorted_arr = sorted(arr, key=lambda x: (bin(x)[2:].zfill(8), x))
    return sorted_arr