"""
QUESTION:
Design a function `rotate_array_clockwise(array, index)` that rotates a given array in a clockwise direction by a given index. The function should:

* Rotate the array in place without using any additional memory.
* Have a time complexity of O(n), where n is the length of the array.
* Work for both positive and negative values of the given index.
* Handle edge cases such as an empty array or an index greater than the array length.
"""

def rotate_array_clockwise(array, index):
    if len(array) == 0 or abs(index) >= len(array):
        return array
    
    if index < 0:
        index = len(array) + index
    
    index = index % len(array)
    
    # Reverse the entire array
    reverse_array(array, 0, len(array) - 1)
    
    # Reverse the first part of the array
    reverse_array(array, 0, index - 1)
    
    # Reverse the second part of the array
    reverse_array(array, index, len(array) - 1)
    
    return array

def reverse_array(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1