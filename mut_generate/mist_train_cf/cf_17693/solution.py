"""
QUESTION:
Write a function `combine_lists` that takes two lists of dictionaries `list1` and `list2` as input, and returns a dictionary where the keys are tuples of the "id", "name", and "age" attributes from `list1`, and the values are the corresponding dictionaries from `list2` with these attributes removed. The function should combine the lists based on matching "id", "name", and "age" attributes.
"""

def combine_lists(list1, list2):
    """
    Combines two lists of dictionaries into a dictionary where the keys are tuples of the "id", "name", and "age" attributes 
    from list1, and the values are the corresponding dictionaries from list2 with these attributes removed.

    Args:
        list1 (list): The list of dictionaries to get the keys from.
        list2 (list): The list of dictionaries to get the values from.

    Returns:
        dict: A dictionary with combined keys and values from list1 and list2.
    """
    combined_dict = {}
    
    for element1 in list1:
        for element2 in list2:
            if (element1.get("id") == element2.get("id") and 
                element1.get("name") == element2.get("name") and 
                element1.get("age") == element2.get("age")):
                key = (element1["id"], element1["name"], element1["age"])
                combined_dict[key] = {k: v for k, v in element2.items() if k not in ["id", "name", "age"]}
    
    return combined_dict