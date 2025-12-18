"""
QUESTION:
Write a function `flatten_convert(array)` that takes a multi-dimensional array of string type elements as input and returns a single dimensional array of integer type elements. The function should handle null and undefined string values in the input array. The solution should be efficient enough to handle large datasets.
"""

def flatten_convert(array):
    """
    This function takes a multi-dimensional array of string type elements, 
    handles null and undefined string values, and returns a single dimensional 
    array of integer type elements.
    
    Args:
        array (list): A multi-dimensional array of string type elements.
    
    Returns:
        list: A single dimensional array of integer type elements.
    """
    flat_list = []
    for sublist in array:
        for item in sublist:
            if item is not None and item != 'None':
                try:
                    flat_list.append(int(item))
                except ValueError:
                    # Handle the exception when item cannot be converted to int
                    pass
    return flat_list