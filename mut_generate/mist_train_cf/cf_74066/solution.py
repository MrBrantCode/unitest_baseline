"""
QUESTION:
Write a function `update_json_key` that takes a JSON object and three key names as input. The function should add the integer values of the first two keys and update the value of the third key with the result. The keys must exist in the JSON object and have integer values. The function should return the updated JSON object.
"""

def update_json_key(json_object, key1, key2, key3):
    """
    Updates the value of key3 in the JSON object with the sum of key1 and key2.

    Args:
        json_object (dict): The JSON object to update.
        key1 (str): The first key to add.
        key2 (str): The second key to add.
        key3 (str): The key to update with the result.

    Returns:
        dict: The updated JSON object.
    """
    json_object[key3] = json_object[key1] + json_object[key2]
    return json_object