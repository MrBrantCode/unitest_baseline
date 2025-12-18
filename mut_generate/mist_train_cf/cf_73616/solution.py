"""
QUESTION:
Write a function `manipulate_json` that takes a JSON object with keys "key1", "key2", and "key3" as input, adds the values of "key1" and "key2", and stores the result in "key3". The function should return the manipulated JSON object.
"""

import json

def manipulate_json(data):
    """
    Manipulates a JSON object by adding the values of 'key1' and 'key2' and storing the result in 'key3'.

    Args:
        data (dict): A JSON object with keys 'key1', 'key2', and 'key3'.

    Returns:
        dict: The manipulated JSON object.
    """
    data['key3'] = data['key1'] + data['key2']
    return data