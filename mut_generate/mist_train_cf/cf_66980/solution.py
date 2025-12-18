"""
QUESTION:
Write a function called `validate_element` that checks if a specified element is present in a given array. The function should take two parameters: `array` (the list of elements to search in) and `element` (the element to search for). The function should return a boolean value indicating whether the element is present in the array.
"""

def validate_element(array, element):
    """
    Checks if a specified element is present in a given array.
    
    Args:
        array (list): The list of elements to search in.
        element: The element to search for.
    
    Returns:
        bool: Whether the element is present in the array.
    """
    return element in array