"""
QUESTION:
Create a function called `rotate_array` that takes two parameters: `arr` (the input array) and `positions` (the number of positions to rotate to the right). The function should rotate the input array in place to the right by the specified number of positions. If the number of positions is negative, the function should rotate the array to the left instead. The function should handle edge cases where the number of positions is larger than the length of the array, and it should not use any built-in array manipulation functions. The time complexity of the function should be O(n), where n is the length of the array.
"""

def rotate_array(arr, positions):
    if len(arr) <= 1:
        return arr
    
    # Normalize the number of positions
    positions = positions % len(arr)
    
    if positions == 0:
        return arr
    
    if positions < 0:
        positions = len(arr) + positions
    
    # Reverse the entire array
    _reverse_array(arr, 0, len(arr)-1)
    
    # Reverse the first part of the array
    _reverse_array(arr, 0, positions-1)
    
    # Reverse the second part of the array
    _reverse_array(arr, positions, len(arr)-1)
    
    return arr

def _reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1