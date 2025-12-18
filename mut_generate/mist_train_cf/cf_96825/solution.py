"""
QUESTION:
Write a function `get_data` that retrieves the data of the third element in a deeply nested JSON array within a deeply nested JSON object. The function should take two parameters: `json_data` and `index`, where `json_data` is the JSON object and `index` is the index of the desired element in the array. The function should return the data at the specified index in the array. The solution should minimize memory usage and the number of iterations required to access the desired data. Assume the JSON structure will always be valid.
"""

def get_data(json_data, index):
    if isinstance(json_data, list):  
        if index < len(json_data):  
            return json_data[index]
        else:
            return None
    elif isinstance(json_data, dict):  
        for key, value in json_data.items():
            result = get_data(value, index)  
            if result is not None:
                return result
    return None