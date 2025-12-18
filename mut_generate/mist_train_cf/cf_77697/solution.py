"""
QUESTION:
Design a function called `find_max_and_indices` that takes an array of integers as input and returns the maximum value in the array along with its indices. If the input array is empty, return an error message. The function should handle large arrays efficiently.
"""

def find_max_and_indices(array):
    """
    This function takes an array of integers as input and returns the maximum value in the array along with its indices.
    
    Parameters:
    array (list): A list of integers.
    
    Returns:
    tuple: A tuple containing the maximum value and its indices. If the input array is empty, returns an error message.
    """
    # Empty array edge case
    if not array:
        return "Cannot find max value and indices in an empty array"

    max_value = array[0]
    indices = [0]

    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
            indices = [i]  # Reset indices
        elif array[i] == max_value:
            indices.append(i)

    return max_value, indices