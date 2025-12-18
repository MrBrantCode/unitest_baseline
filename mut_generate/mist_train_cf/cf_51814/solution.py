"""
QUESTION:
Create a function `create_index_dict` that takes a list of elements as input and returns a dictionary where keys are the elements and values are lists of their corresponding indices in the original list. If an element appears multiple times in the list, all its indices should be included in the corresponding list. The function should handle duplicate elements correctly.
"""

def create_index_dict(input_list):
    """
    Creates a dictionary where keys are elements from the input list and values are lists of their corresponding indices.

    Args:
        input_list (list): A list of elements.

    Returns:
        dict: A dictionary with elements as keys and lists of indices as values.
    """
    index_dict = {}
    for i, element in enumerate(input_list):
        if element in index_dict:
            index_dict[element].append(i)
        else:
            index_dict[element] = [i]
    return index_dict