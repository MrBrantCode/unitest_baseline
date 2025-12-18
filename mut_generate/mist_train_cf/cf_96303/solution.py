"""
QUESTION:
Implement a function `reverse_array(arr)` that takes an array as input and reverses the order of its elements in-place, without using any built-in functions or methods and without creating any additional arrays or data structures. The function should modify the input array directly and return the reversed array.
"""

def reverse_array(arr):
    # Check if the array is empty or has only one element
    if len(arr) <= 1:
        return arr
    
    # Swap the elements from the beginning and end of the array
    start = 0
    end = len(arr) - 1
    
    while start < end:
        # Swap the elements using a temporary variable
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        
        # Move the indices towards each other
        start += 1
        end -= 1
    
    return arr