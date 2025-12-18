"""
QUESTION:
Write a function `identify_data_types` that takes one argument and returns the data type of the input as a string. The input can be a string, number (integer or float), boolean, list, or dictionary, and can contain nested structures. If the input is a list, return a list of data types.
"""

def identify_data_types(data):
    if isinstance(data, str):
        return "String"
    elif isinstance(data, int) or isinstance(data, float):
        return "Number" if isinstance(data, int) else "Float"
    elif isinstance(data, bool):
        return "Boolean"
    elif isinstance(data, list):
        return [identify_data_types(i) for i in data]
    elif isinstance(data, dict):
        return "Dictionary"
    else:
        return "Unknown type"