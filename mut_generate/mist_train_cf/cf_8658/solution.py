"""
QUESTION:
Rotate a given array in clockwise direction by a given index without using any additional memory. The function should work for both positive and negative values of the given index, handle edge cases such as an empty array or an index greater than the array length, and handle arrays with duplicate values.

The function should be named `rotate_array` and take two parameters: `array` and `index`. It should return the rotated array. The time complexity of the function should be O(n), where n is the length of the array.
"""

def rotate_array(array, index):
    """
    Rotate a given array in clockwise direction by a given index.

    Parameters:
    array (list): The input array to be rotated.
    index (int): The number of steps to rotate the array.

    Returns:
    list: The rotated array.
    """
    if len(array) == 0 or abs(index) >= len(array):
        return array
    
    effective_index = index % len(array)
    if effective_index < 0:
        effective_index += len(array)
    
    array.reverse()
    array[:effective_index] = array[:effective_index][::-1]
    array[effective_index:] = array[effective_index:][::-1]
    
    return array