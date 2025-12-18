"""
QUESTION:
Write a function called `delete_elements_at_indices` that takes a list and a list of indices as input, removes elements from the list at the specified indices, handles out-of-range indices by printing an error message, and returns the modified list. The function should delete elements in a way that does not affect the indices of subsequent elements to be deleted.
"""

def delete_elements_at_indices(input_list, indices):
    """
    Deletes elements from the input list at the specified indices.

    Args:
    input_list (list): The list from which elements are to be deleted.
    indices (list): A list of indices at which elements are to be deleted.

    Returns:
    list: The modified list after deleting elements at the specified indices.
    """
    for index in sorted(indices, reverse=True):
        if index < len(input_list):
            del input_list[index]
        else:
            print(f"Index {index} is out of range.")
    return input_list