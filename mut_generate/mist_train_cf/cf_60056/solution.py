"""
QUESTION:
Create a function named `shortest_data_structure` that takes a dictionary as input, where keys are data structure names and values are lists of operations. The function should return the name of the data structure with the shortest name.
"""

def shortest_data_structure(data_structures):
    """
    Returns the name of the data structure with the shortest name.

    Args:
    data_structures (dict): A dictionary where keys are data structure names and values are lists of operations.

    Returns:
    str: The name of the data structure with the shortest name.
    """
    return min(data_structures, key=len)