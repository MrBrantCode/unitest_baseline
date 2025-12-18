"""
QUESTION:
Write a function `delete_elements` that takes a list and a list of indices as input, deletes the elements at the given indices from the list, and returns the modified list. If an index is out of range, the function should print an error message and continue deleting elements from the remaining valid indices. The function should have a time complexity of O(n), where n is the length of the list.
"""

def delete_elements(lst, indices):
    """
    Deletes elements at given indices from the list and returns the modified list.
    
    Args:
    lst (list): The input list.
    indices (list): A list of indices to be deleted.
    
    Returns:
    list: The modified list after deletion.
    """
    for index in sorted(indices, reverse=True):
        try:
            del lst[index]
        except IndexError:
            print(f"Index {index} is out of range.")
    return lst