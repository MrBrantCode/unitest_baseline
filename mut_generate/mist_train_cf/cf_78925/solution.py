"""
QUESTION:
Write a function `update_key3` that takes a JSON object as input, adds the numeric values of `'subkey1'` from `'key7'` and `'subsubkey1'` from `'subkey2'`, which is part of `'key5'`, and replaces the value of `'key3'` with the sum. The function should handle cases where the specified keys are not found in the provided JSON object.
"""

import json

def update_key3(data):
    """
    Update 'key3' in the given JSON object with the sum of 'subkey1' from 'key7' and 'subsubkey1' from 'subkey2' which is part of 'key5'.

    Args:
        data (dict): The JSON object.

    Returns:
        dict: The updated JSON object.
    """
    try:
        value1 = data['key7']['subkey1']['subsubkey1']
        value2 = data['key5']['subkey2']['subsubkey1']
        data['key3'] = value1 + value2
    except KeyError as e:
        print(f"Key {e} not found in JSON data.")
    return data