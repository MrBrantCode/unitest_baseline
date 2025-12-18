"""
QUESTION:
Swap the positions of two elements at the specified indices in a given array of at least 1000 integers, without using a temporary variable, and with a time complexity of O(1) and space complexity of O(1). The function should be named `swap_elements` and take three parameters: the array and the two indices. The original array should remain unchanged except for the swapped elements.
"""

def swap_elements(array, index1, index2):
    if index1 < 0 or index1 >= len(array) or index2 < 0 or index2 >= len(array):
        return array

    array[index1] = array[index1] ^ array[index2]
    array[index2] = array[index1] ^ array[index2]
    array[index1] = array[index1] ^ array[index2]

    return array