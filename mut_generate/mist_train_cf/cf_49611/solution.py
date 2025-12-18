"""
QUESTION:
Create a function `create_type_register` that takes a list of elements as input and returns a dictionary where the keys are the indices of the elements in the list and the values are the corresponding data types.
"""

def create_type_register(elements):
    """
    Create a dictionary where the keys are the indices of the elements in the list 
    and the values are the corresponding data types.

    Args:
        elements (list): A list of elements.

    Returns:
        dict: A dictionary with indices as keys and data types as values.
    """
    register = {}
    for i, element in enumerate(elements):
        register[i] = type(element)
    return register