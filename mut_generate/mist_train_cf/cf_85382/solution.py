"""
QUESTION:
Create a function `parse_json` that converts a given JSON string to a Python dictionary and logs any JSON decoding errors. The function should return an empty dictionary if a decoding error occurs. 

Create another function `extract_info` that takes a dictionary and a list of keys as input and returns the nested dictionary corresponding to the last key in the list. If any key in the list does not exist in the dictionary, the function should log an error and return an empty dictionary.

Both functions should be robust enough to handle missing or malformed input without crashing.
"""

import json
import logging

# Initialize logger
logger = logging.getLogger()

def parse_json(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        logger.error(f'Error decoding JSON: {str(e)}')
        return {}

def extract_info(data, keys=['employee']):
    try:
        for key in keys:
            data = data[key]
        return data
    except KeyError as e:
        logger.error(f'KeyError: {str(e)}')
        return {}