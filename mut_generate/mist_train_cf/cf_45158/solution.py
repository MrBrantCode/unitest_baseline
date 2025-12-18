"""
QUESTION:
Write a function called `find_position` that takes an array and a specific value as input, and returns the position(s) of the value within the array. Note that Python uses zero-based indexing, and if the value appears multiple times, the function should return all its positions.
"""

def find_position(array, specific_value):
    """
    Returns the position(s) of a specific value within an array.
    
    Args:
        array (list): The input array to search in.
        specific_value: The value to search for.
    
    Returns:
        list: A list of indices where the specific value is found.
    """
    return [i for i, x in enumerate(array) if x == specific_value]