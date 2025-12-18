"""
QUESTION:
Create a function `join_elements` that transforms an array of strings into a singular continuous textual representation. The function should take an array of strings and a delimiter as input, and return a string where all elements from the array are joined with the specified delimiter in between.
"""

def join_elements(array, delimiter):
    """
    This function transforms an array of strings into a singular continuous textual representation.
    
    Args:
        array (list): A list of strings to be joined.
        delimiter (str): A delimiter to be used in between the array elements.
    
    Returns:
        str: A string where all elements from the array are joined with the specified delimiter in between.
    """
    return delimiter.join(array)