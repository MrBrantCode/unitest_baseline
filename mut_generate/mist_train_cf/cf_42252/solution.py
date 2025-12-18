"""
QUESTION:
Implement a function `extract_info(data: dict) -> dict` where `data` is a dictionary containing string keys and various types of values, with a length between 1 and 100. The function should extract variable names, numeric values, and string values from the dictionary and return them in a new dictionary with the keys "variables", "numeric_values", and "string_values" respectively.
"""

def extract_info(data: dict) -> dict:
    variables = list(data.keys())
    numeric_values = [value for value in data.values() if isinstance(value, (int, float))]
    string_values = [value for value in data.values() if isinstance(value, str)]
    
    return {
        "variables": variables,
        "numeric_values": numeric_values,
        "string_values": string_values
    }