"""
QUESTION:
Create a function called `transpose_and_reverse` that takes a 3D array as input and returns the array after performing a transpose and reverse operation on each 2D layer within the array. The transpose operation should swap the rows and columns of each 2D layer, and the reverse operation should reverse the order of elements in each row of the transposed 2D layer. The function should return the resulting 3D array.
"""

def transpose_and_reverse(array_3d):
    """
    This function takes a 3D array, performs a transpose and reverse operation 
    on each 2D layer within the array, and returns the resulting 3D array.

    Args:
        array_3d (list): A 3D array

    Returns:
        list: The resulting 3D array after transpose and reverse operations
    """
    return [[[row[i] for row in reversed(layer)] for i in range(len(layer[0]))] for layer in array_3d]