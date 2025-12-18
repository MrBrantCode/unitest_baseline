"""
QUESTION:
Write a function `reverse_and_sort(arr, pos)` that takes two parameters: an array `arr` and a position `pos`. The function should reverse the elements of `arr` up to the specified `pos` and sort the remaining elements in ascending order. 

The function must handle edge cases such as an empty array, an array with a single element, or a `pos` that exceeds the array's boundaries. It must also be able to handle arrays containing duplicate elements, negative integers, and floating point numbers. If the array contains non-numeric elements, the function should return an error message.
"""

def reverse_and_sort(arr, pos):
    if not arr:
        return []
        
    if pos > len(arr):
        pos = len(arr)
        
    if isinstance(arr[0], (float, int)):
        arr[:pos] = arr[:pos][::-1]
        arr[pos:] = sorted(arr[pos:])
        return arr
    else:
        return "Only arrays of integers or floating point numbers are supported."