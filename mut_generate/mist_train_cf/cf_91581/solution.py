"""
QUESTION:
Create a dictionary from a given list where the list elements are the keys and their corresponding indexes are the values. The function should take a list as input and return a dictionary. The function name should be `generate_index_dict`. The list can contain any hashable elements.
"""

def generate_index_dict(input_list):
    """
    Creates a dictionary from a given list where the list elements are the keys and their corresponding indexes are the values.
    
    Args:
        input_list (list): A list of hashable elements.
    
    Returns:
        dict: A dictionary where the keys are the elements from the input list and the values are their corresponding indexes.
    """
    return {input_list[i]: i for i in range(len(input_list))}