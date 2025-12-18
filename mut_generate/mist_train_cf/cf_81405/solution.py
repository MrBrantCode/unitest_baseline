"""
QUESTION:
Write a recursive function `extract_values` to extract the values of specific keys from a nested JSON object. The function should take two parameters: `json_data` (the JSON object) and `keys_to_extract` (a list of keys to extract). The function should be able to handle any depth of nesting in the JSON data and return a dictionary with the extracted key-value pairs. If a key does not exist in the JSON data, it should not be included in the returned dictionary.
"""

def extract_values(json_data, keys_to_extract):
    extracted = {}
    
    # Iterate over each key-value pair in the json_data
    for key, value in json_data.items():
        # If the value is a dictionary (i.e., a nested JSON object), then
        # use recursion to extract keys from this nested object
        if isinstance(value, dict):
            extracted.update(extract_values(value, keys_to_extract))
        # If the key is in the list of keys to extract, then store it
        elif key in keys_to_extract:
            extracted[key] = value
    
    return extracted