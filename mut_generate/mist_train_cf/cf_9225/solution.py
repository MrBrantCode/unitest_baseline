"""
QUESTION:
Write a function named `find_max_element` that takes an array of integers as input and returns the maximum element in the array, where the maximum element is the one with the largest absolute value. The function should be able to handle arrays containing negative numbers.
"""

def find_max_element(array):
    """
    This function finds the maximum element in an array based on absolute values.
    
    Parameters:
    array (list): A list of integers.
    
    Returns:
    int: The maximum element in the array with the largest absolute value.
    """
    max_element = array[0]
    for element in array[1:]:
        if abs(element) > abs(max_element):
            max_element = element
    return max_element