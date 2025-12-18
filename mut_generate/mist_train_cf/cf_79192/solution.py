"""
QUESTION:
Create a function `modify_value` that takes a JSON object and three keys as input, and returns the modified JSON object. The function should add the values of the second and third keys to the first key. 

The function should also perform the following validations:
- Check if the input is a valid JSON object.
- Check if all three keys exist in the JSON object.
- Check if the values of all three keys are integers.

If any of these validations fail, the function should return an error message.
"""

import json

def modify_value(json_obj, target_key, key1, key2):
    """
    This function modifies a given JSON object by adding the values of key1 and key2 to the value of target_key.
    
    Args:
        json_obj (dict): The input JSON object.
        target_key (str): The key whose value is to be modified.
        key1 (str): The first key whose value is to be added.
        key2 (str): The second key whose value is to be added.
    
    Returns:
        dict or str: The modified JSON object if all validations pass, otherwise an error message.
    """

    # Check if the input is a valid JSON object.
    if not isinstance(json_obj, dict):
        return "Error: Invalid JSON object"

    # Check if all three keys exist in the JSON object.
    if target_key not in json_obj or key1 not in json_obj or key2 not in json_obj:
        return "Invalid Key Error"

    # Check if the values of all three keys are integers.
    if not isinstance(json_obj[target_key], int) or not isinstance(json_obj[key1], int) or not isinstance(json_obj[key2], int):
        return "Error, Only Integer Values Accepted"

    # Add the values of key1 and key2 to the value of target_key.
    json_obj[target_key] = json_obj[key1] + json_obj[key2]
    return json_obj