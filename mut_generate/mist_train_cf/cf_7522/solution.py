"""
QUESTION:
Write a function `reverse_and_sort_json_objects` that takes a list of JSON objects as input. The function should return a single JSON document that contains the objects in reverse order, with each object's key-value pairs sorted alphabetically by keys in descending order.
"""

import json

def reverse_and_sort_json_objects(json_objects):
    """
    This function takes a list of JSON objects, reverses their order, 
    sorts each object's key-value pairs alphabetically by keys in descending order, 
    and returns a single JSON document.

    Args:
        json_objects (list): A list of JSON objects.

    Returns:
        str: A single JSON document containing the objects in reverse order, 
             with each object's key-value pairs sorted alphabetically by keys in descending order.
    """

    # Reverse the order of the input list
    reversed_list = json_objects[::-1]

    # Sort each object's key-value pairs alphabetically by keys in descending order
    sorted_list = [dict(sorted(obj.items(), key=lambda x: x[0], reverse=True)) for obj in reversed_list]

    # Combine the objects into a single JSON document
    output_json = json.dumps({k: v for obj in sorted_list for k, v in obj.items()})

    return output_json