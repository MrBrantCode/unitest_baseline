"""
QUESTION:
Create a function named `sort_dict_by_value` that takes a dictionary as input and returns a list of tuples. The list should be sorted in ascending order based on the dictionary's values. If the dictionary is empty, the function should return an empty list. The function should not modify the original dictionary.
"""

def sort_dict_by_value(dictionary):
    """
    This function takes a dictionary as input, sorts its items based on the values in ascending order, 
    and returns the result as a list of tuples.

    Args:
        dictionary (dict): The dictionary to be sorted.

    Returns:
        list: A list of tuples, where each tuple contains a key-value pair from the dictionary, 
              sorted in ascending order based on the dictionary's values.
    """
    return sorted(dictionary.items(), key=lambda x: x[1])