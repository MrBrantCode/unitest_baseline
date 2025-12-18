"""
QUESTION:
Create a function called "parse_json_data" that takes a JSON object as input. The function should transform every value in the JSON object into a string and iterate over the items in the 'locations' array, assigning an additional string marking their index position within the array. The 'locations' array should be transformed into a list of strings in the format 'Location [index]: [original string]'. The output should be a dictionary called "parsed_data".
"""

import json

def parse_json_data(data):
    """
    This function takes a JSON object as input, transforms every value into a string, 
    and formats the 'locations' array with index markers.
    
    Args:
        data (dict): A dictionary representing the JSON object.
    
    Returns:
        dict: A dictionary with string values and formatted 'locations' array.
    """
    parsed_data = {}
    for key, value in data.items():
        if key == 'locations':
            parsed_data[key] = ['Location {}: {}'.format(index, loc) for index, loc in enumerate(value)]
        else:
            parsed_data[key] = str(value)
    return parsed_data