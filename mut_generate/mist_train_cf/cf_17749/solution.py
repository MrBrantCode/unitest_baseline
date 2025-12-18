"""
QUESTION:
Create a function called create_index_dict that takes a list as input and returns a dictionary where the keys are the list elements and the values are the corresponding list indexes. The function should not assume the list elements are unique.
"""

def create_index_dict(lst):
    """
    This function takes a list as input and returns a dictionary where the keys are the list elements and the values are the corresponding list indexes.

    Args:
        lst (list): The input list.

    Returns:
        dict: A dictionary where the keys are the list elements and the values are the corresponding list indexes.
    """
    index_dict = {}
    for i, elem in enumerate(lst):
        index_dict[elem] = i
    return index_dict