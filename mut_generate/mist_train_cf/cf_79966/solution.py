"""
QUESTION:
Write a Python function named max_array_elements that calculates the maximum number of elements of a given type that can be accommodated in a one-dimensional array, assuming the maximum array size is limited by the maximum integer size and available memory. The function should take the size of each element in bytes and the available memory in bytes as parameters.
"""

def max_array_elements(element_size, available_memory):
    """
    Calculate the maximum number of elements of a given type that can be accommodated in a one-dimensional array.
    
    Parameters:
    element_size (int): The size of each element in bytes.
    available_memory (int): The available memory in bytes.
    
    Returns:
    int: The maximum number of elements that can be accommodated in the array.
    """
    import sys
    max_integer_size = sys.maxsize
    max_elements_by_integer_size = max_integer_size // element_size
    max_elements_by_available_memory = available_memory // element_size
    return min(max_elements_by_integer_size, max_elements_by_available_memory)