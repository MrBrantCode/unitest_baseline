"""
QUESTION:
Create a function called `merge_entities` that takes two JSON strings as input, compares them for equality, and returns a new JSON string that is the result of merging the two input JSON objects. The function should handle duplicate keys by using the values from the second JSON object.
"""

import json

def merge_entities(entity_alpha, entity_beta):
    """
    Merge two JSON strings into one.

    Args:
    entity_alpha (str): The first JSON string.
    entity_beta (str): The second JSON string.

    Returns:
    str: A new JSON string that is the result of merging the two input JSON objects.
    """
    entity_alpha_dict = json.loads(entity_alpha)
    entity_beta_dict = json.loads(entity_beta)
    merged_entity = {**entity_alpha_dict, **entity_beta_dict}
    return json.dumps(merged_entity)