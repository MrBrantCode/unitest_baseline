"""
QUESTION:
Implement the function `check_type(data)` to decode a given JSON object `data`, transform its distinct numeric values into strings, and add 'city' to the 'city' field and 5 to the 'age' field. The function should also handle potential JSON decoding errors and return a dictionary 'parsed_data' containing both the original and modified values.
"""

import json
import copy

def transform_data(data):
    """
    Decodes a given JSON object, transforms its distinct numeric values into strings,
    adds 'city' to the 'city' field and 5 to the 'age' field.

    Args:
        data (str): A JSON object as a string.

    Returns:
        dict: A dictionary containing both the original and modified values.
    """

    # Function to transform data types
    def transform_types(data):
        if type(data) is dict:
            return {k: transform_types(v) for k, v in data.items()}
        elif type(data) is int:
            return str(data)
        elif type(data) is float:
            return str(data)
        elif type(data) is list:
            return [transform_types(i) for i in data]
        elif data is None:
            return ''
        else:
            return data

    try:
        # Load JSON data
        json_data = json.loads(data)
    except json.JSONDecodeError as e:
        print("Invalid JSON", str(e))
        return None

    # Create a deepcopy of data to prevent from modifying original
    parsed_data = copy.deepcopy(json_data)

    # Modify numeric values
    parsed_data['age'] += 5
    for location in parsed_data['locations']:
        location['city'] += ' city'
        location['population'] = str(location['population'])

    # Parse strings from all values
    parsed_data = transform_types(parsed_data)

    # Result
    result = {'original': json_data, 'parsed': parsed_data}
    return result