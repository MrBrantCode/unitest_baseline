"""
QUESTION:
Create a function called `assign_special_values` that takes in a data structure (which can be a list, dictionary, or a nested combination of both) and replaces all special values (empty strings, NaN, and negative numbers) with 0. The function should be able to handle nested lists and dictionaries recursively.
"""

def assign_special_values(data):
    """
    Replaces all special values (empty strings, NaN, and negative numbers) in a given data structure with 0.
    
    Args:
        data (list or dict): The input data structure.
    
    Returns:
        The modified data structure with special values replaced.
    """
    
    if isinstance(data, list):
        for i in range(len(data)):
            if isinstance(data[i], list) or isinstance(data[i], dict):
                data[i] = assign_special_values(data[i])
            elif data[i] == '' or data[i] is None or (isinstance(data[i], (int, float)) and data[i] < 0):
                data[i] = 0
    elif isinstance(data, dict):
        for key in data:
            if isinstance(data[key], list) or isinstance(data[key], dict):
                data[key] = assign_special_values(data[key])
            elif data[key] == '' or data[key] is None or (isinstance(data[key], (int, float)) and data[key] < 0):
                data[key] = 0
    elif data == '' or data is None or (isinstance(data, (int, float)) and data < 0):
        data = 0
    return data