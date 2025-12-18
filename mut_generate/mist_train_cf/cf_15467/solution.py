"""
QUESTION:
Create a function `create_valid_json` that takes a list of dictionaries `data` as input, where each dictionary represents a data entry with keys "Name", "Age", and "Country". 

Validate each data entry to ensure that the "Name" is a non-empty string, the "Age" is a positive integer, and the "Country" is one of "US", "Canada", or "UK". 

Exclude any data entries that fail the validation process and return a JSON object containing the validated data entries as an array of objects. The function should have a time complexity of O(n), where n is the number of data entries.
"""

import json

def create_valid_json(data):
    """
    This function takes a list of dictionaries as input, validates each data entry, 
    and returns a JSON object containing the validated data entries as an array of objects.
    
    Args:
        data (list): A list of dictionaries, where each dictionary represents a data entry 
                     with keys "Name", "Age", and "Country".
    
    Returns:
        str: A JSON object containing the validated data entries as an array of objects.
    """
    valid_data = []
    for entry in data:
        if (isinstance(entry["Name"], str) and entry["Name"] != "" and 
            isinstance(entry["Age"], int) and entry["Age"] > 0 and 
            entry["Country"] in ["US", "Canada", "UK"]):
            valid_data.append(entry)
    return json.dumps(valid_data)