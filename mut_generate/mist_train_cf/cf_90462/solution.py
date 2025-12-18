"""
QUESTION:
Implement the `reverse_array` function to reverse the order of elements in a given array. The function should use recursion and have a time complexity of O(n), where n is the length of the array. It should not use any additional data structures or built-in functions.
"""

def reverse_array(arr, start=0, end=None):
    # Base case: if start and end are the same or adjacent, we have reversed the array
    if end is None:
        end = len(arr) - 1
    if start >= end:
        return arr
    
    # Swap the elements at the start and end indices
    arr[start], arr[end] = arr[end], arr[start]
    
    # Recursively call the function with updated start and end indices
    return reverse_array(arr, start+1, end-1)