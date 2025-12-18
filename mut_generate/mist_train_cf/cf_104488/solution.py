"""
QUESTION:
Write a function `delete_elements` that takes a list and a list of indices as input and returns the list with elements at the specified indices deleted. The function should handle index shifting after each deletion.
"""

def delete_elements(lst, indices):
    """
    Deletes elements at specified indices from the list and handles index shifting after each deletion.

    Args:
        lst (list): The input list.
        indices (list): A list of indices to delete from the list.

    Returns:
        list: The list with elements at the specified indices deleted.
    """
    indices.sort(reverse=True)  # Sort indices in descending order to avoid index shifting issues
    for index in indices:
        del lst[index]
    return lst