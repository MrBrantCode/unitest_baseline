"""
QUESTION:
Create a function called `reverse_array` that takes an array as input and reverses the order of its elements without using any built-in array reverse function or additional data structures. The function should modify the original array in-place.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        # Swap elements
        arr[start], arr[end] = arr[end], arr[start]
        
        # Move towards the middle
        start += 1
        end -= 1
    
    return arr