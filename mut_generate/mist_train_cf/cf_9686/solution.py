"""
QUESTION:
Create a function called `sort_dict_by_keys` that takes a dictionary as input and returns a list of tuples, where each tuple contains a key-value pair from the dictionary. The list should be sorted in descending order based on the dictionary keys.
"""

def sort_dict_by_keys(input_dict):
    """
    This function takes a dictionary as input and returns a list of tuples, 
    where each tuple contains a key-value pair from the dictionary. 
    The list is sorted in descending order based on the dictionary keys.

    Args:
        input_dict (dict): The input dictionary to be sorted.

    Returns:
        list: A list of tuples containing key-value pairs from the dictionary, sorted in descending order by keys.
    """
    return sorted(input_dict.items(), reverse=True)