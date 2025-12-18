"""
QUESTION:
Implement a function named `search_nested_list` that performs a linear search on a nested list. The function should take two parameters: `nested_list` and `target`. It should work with multiple data types, including integers and strings. If the target is found, return a tuple containing the found value and its location in the nested list (as a tuple of indices). If the target is not found, return the message 'Value not found'.
"""

def search_nested_list(nested_list, target):
    """
    Performs a linear search on a nested list.

    Args:
        nested_list (list): A nested list containing various data types.
        target: The value to be searched in the nested list.

    Returns:
        tuple: A tuple containing the found value and its location in the nested list.
        str: 'Value not found' if the target is not found in the nested list.
    """
    for i in range(len(nested_list)):
        for j in range(len(nested_list[i])):
            if nested_list[i][j] == target:
                return (target, (i, j))
    return 'Value not found'