"""
QUESTION:
Write a function `combine_objects` that combines two input dictionaries into one dictionary, based on the "name" property being case-sensitive and identical in both objects. The function should only include the "name" property if it has the same value and case in both input dictionaries.
"""

def combine_objects(obj1, obj2):
    """
    This function combines two input dictionaries into one dictionary, 
    based on the "name" property being case-sensitive and identical in both objects.

    Args:
        obj1 (dict): The first input dictionary.
        obj2 (dict): The second input dictionary.

    Returns:
        dict: A dictionary containing the combined objects.
    """
    combined_obj = {}
    for obj in [obj1, obj2]:
        for key, value in obj.items():
            if key == "name" and key in combined_obj and combined_obj[key] == value:
                combined_obj[key] = value
            elif key == "name" and key not in combined_obj:
                combined_obj[key] = value
            elif key != "name":
                combined_obj[key] = value

    return combined_obj