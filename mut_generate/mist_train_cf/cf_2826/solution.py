"""
QUESTION:
Create a function `combine_lists` that takes two lists of dictionaries (`list1` and `list2`) and a list of common attributes (`common_attributes`). The function should combine `list1` and `list2` into a dictionary where each key is a tuple of the common attributes from `list1` and each value is the corresponding dictionary from `list2` without the common attributes. 

The function should return the combined dictionary. The order of the elements in the resulting dictionary does not matter.

The function should assume that the common attributes exist in both lists and that there is a match for each element in `list1` in `list2` based on the common attributes.
"""

def combine_lists(list1, list2, common_attributes):
    """
    Combines two lists of dictionaries into a dictionary where each key is a tuple 
    of the common attributes from list1 and each value is the corresponding 
    dictionary from list2 without the common attributes.

    Args:
    list1 (list): The first list of dictionaries.
    list2 (list): The second list of dictionaries.
    common_attributes (list): A list of common attributes between the two lists.

    Returns:
    dict: A dictionary where each key is a tuple of the common attributes from list1 
    and each value is the corresponding dictionary from list2 without the common attributes.
    """
    combined_dict = {}
    for item1 in list1:
        for item2 in list2:
            if all(item1[key] == item2[key] for key in common_attributes):
                key = tuple(item1[key] for key in common_attributes)
                value = {k: v for k, v in item2.items() if k not in common_attributes}
                combined_dict[key] = value
    return combined_dict