"""
QUESTION:
Design a function named `rotate_array_clockwise` that takes an array and an integer index as input. Rotate the array in a clockwise direction by the given index, in place, without using any additional memory. The function should work for both positive and negative values of the index and handle edge cases such as an empty array or an index greater than the array length. The time complexity should be O(n), where n is the length of the array.
"""

def rotate_array_clockwise(array, index):
    if len(array) == 0 or index >= len(array):
        return array
    
    if index < 0:
        index = len(array) + index
    
    index = index % len(array)
    
    def reverse_array(start, end):
        while start < end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1

    # Reverse the entire array
    reverse_array(0, len(array) - 1)
    
    # Reverse the first part of the array
    reverse_array(0, index - 1)
    
    # Reverse the second part of the array
    reverse_array(index, len(array) - 1)

    return array