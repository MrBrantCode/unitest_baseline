"""
QUESTION:
Create a function called `copy_2d_array` that takes a 2D array as input and returns a separate instance in memory that is a copy of the input array. The function should create a new list and append copied rows to it, with each row being a new list that contains the elements of the original row. The copied array should have the same values as the original array but be a separate instance in memory.
"""

def copy_2d_array(array):
    """
    Creates a separate instance in memory that is a copy of the input 2D array.
    
    Args:
    array (list): The input 2D array to be copied.
    
    Returns:
    list: A separate instance in memory that is a copy of the input array.
    """
    copy_array = []
    for row in array:
        row_copy = []
        for element in row:
            row_copy.append(element)
        copy_array.append(row_copy)
    return copy_array