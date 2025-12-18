"""
QUESTION:
Create a function called `reverse_and_sort_json_objects` that takes a list of JSON objects as input. The function should return a JSON document where the list of objects is in reverse order and each object is ordered alphabetically by their keys. The keys in each object should be unique and the objects should not be merged.
"""

import json

def reverse_and_sort_json_objects(objects):
    """
    This function takes a list of JSON objects as input, reverses the order of the list, 
    and sorts each object by their keys in alphabetical order.

    Args:
        objects (list): A list of JSON objects.

    Returns:
        list: The reversed and sorted list of JSON objects.
    """

    # Reverse the order of the list
    reversed_objects = objects[::-1]

    # Sort each object by their keys in alphabetical order
    sorted_objects = [dict(sorted(obj.items())) for obj in reversed_objects]

    return sorted_objects