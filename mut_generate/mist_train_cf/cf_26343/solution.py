"""
QUESTION:
Create a function named `allocate` that takes a list of lists (`data`) as input, where each sublist contains a string and an integer. The function should calculate the proportion of the total integer value for each sublist and return a list of these proportions. The input list will not be empty and will contain at least one sublist.
"""

def allocate(data):
    """
    Calculate the proportion of the total integer value for each sublist.

    Args:
        data (list of lists): A list of sublists, where each sublist contains a string and an integer.

    Returns:
        list: A list of proportions of the total integer value for each sublist.
    """
    total = sum(item[1] for item in data)
    return [item[1] / total for item in data]