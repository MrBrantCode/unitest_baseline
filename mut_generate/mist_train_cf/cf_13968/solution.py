"""
QUESTION:
Write a function `extract_value(data, key)` that takes a JSON object `data` and a key `key` as input, and returns a list of values associated with the given `key`. The function should be able to handle nested JSON objects and arrays. The function should not use any external libraries other than the built-in Python libraries.
"""

def extract_value(data, key):
    """
    Extracts a list of values associated with the given key from a JSON object.
    
    Args:
    data (dict or list): The JSON object to extract values from.
    key (str): The key to extract values for.
    
    Returns:
    list: A list of values associated with the given key.
    """
    values = []
    
    if isinstance(data, dict):
        if key in data:
            values.append(data[key])
        for k, v in data.items():
            if isinstance(v, (dict, list)):
                values.extend(extract_value(v, key))
                
    elif isinstance(data, list):
        for item in data:
            values.extend(extract_value(item, key))
    
    return values