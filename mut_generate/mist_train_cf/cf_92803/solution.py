"""
QUESTION:
Write a function called `count_unique_elements` that takes a 2D array of positive integers as input, where each sub-array contains exactly two elements. The function should return the total number of unique elements in the array.
"""

def count_unique_elements(array):
    """
    This function calculates the total number of unique elements in a 2D array of positive integers.
    
    Parameters:
    array (list): A 2D array of positive integers, where each sub-array contains exactly two elements.
    
    Returns:
    int: The total number of unique elements in the array.
    """
    unique_elements = set()
    
    for sub_array in array:
        unique_elements.add(sub_array[0])
        unique_elements.add(sub_array[1])
    
    return len(unique_elements)