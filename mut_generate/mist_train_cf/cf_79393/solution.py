"""
QUESTION:
Create a function named `augment_tuple` that takes two parameters: an existing tuple and a new element. The function should return a new tuple with the new element added at the beginning of the existing tuple. The existing tuple should remain unchanged due to its immutable nature.
"""

def augment_tuple(existing_tuple, new_element):
    """
    Returns a new tuple with the new element added at the beginning of the existing tuple.
    
    Args:
        existing_tuple (tuple): The original tuple.
        new_element: The new element to be added.

    Returns:
        tuple: A new tuple with the new element added at the beginning.
    """
    return (new_element,) + existing_tuple