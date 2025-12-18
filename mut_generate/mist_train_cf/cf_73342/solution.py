"""
QUESTION:
Write a function called `unique_sum_2d_array` that calculates the sum of all unique elements in a given 2D array. The function should be able to handle both integers and floating point numbers without using any inbuilt or 3rd party libraries. The 2D array can contain duplicate elements and is passed as an argument to the function.
"""

def unique_sum_2d_array(array):
    """
    This function calculates the sum of all unique elements in a given 2D array.
    
    Parameters:
    array (list): A 2D list containing integers and/or floating point numbers.
    
    Returns:
    float: The sum of all unique elements in the 2D array.
    """
    unique_elements = set()
    for sub_array in array:
        for elem in sub_array:
            unique_elements.add(elem)
    return sum(unique_elements)