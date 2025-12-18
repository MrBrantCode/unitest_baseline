"""
QUESTION:
Create a function called `convert_list_to_dictionary` that takes a list as input and returns a dictionary. The dictionary should have the items from the list as keys and their corresponding first occurrence position in the list as values. If an item appears multiple times in the list, only its first occurrence should be included in the dictionary. The dictionary should be sorted in descending order based on the values. If two values are equal, they should be sorted alphabetically in ascending order.
"""

def convert_list_to_dictionary(lst):
    """
    This function takes a list as input and returns a dictionary.
    The dictionary has the items from the list as keys and their corresponding first occurrence position in the list as values.
    If an item appears multiple times in the list, only its first occurrence is included in the dictionary.
    The dictionary is sorted in descending order based on the values. If two values are equal, they are sorted alphabetically in ascending order.

    Args:
        lst (list): The input list.

    Returns:
        dict: A dictionary with items as keys and their first occurrence positions as values.
    """
    unique_items = []
    positions = {}
    
    # Iterate through the list and keep track of the first occurrence of each item and its position
    for i, item in enumerate(lst):
        if item not in unique_items:
            unique_items.append(item)
            positions[item] = i
    
    # Sort the dictionary in descending order based on the values. If two values are equal, sort them alphabetically in ascending order
    sorted_dict = dict(sorted(positions.items(), key=lambda x: (-x[1], x[0])))

    return sorted_dict