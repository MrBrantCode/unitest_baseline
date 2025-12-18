"""
QUESTION:
Write a function called `get_third_element` that retrieves the data of the third element in a nested JSON array within a nested JSON object. The function should take a JSON object as input, where the JSON object has the following structure: 
`{"outerObj": {"innerObj": {"nestedArray": [1, 2, 3, 4, 5]}}}`. The function should return the value of the third element in the "nestedArray" of the "innerObj" of the "outerObj".
"""

import json

def get_third_element(data):
    """
    Retrieves the data of the third element in a nested JSON array within a nested JSON object.

    Args:
        data (dict): A dictionary representing the JSON object.

    Returns:
        The value of the third element in the "nestedArray" of the "innerObj" of the "outerObj".
    """
    data_dict = json.loads(json.dumps(data))
    return data_dict['outerObj']['innerObj']['nestedArray'][2]