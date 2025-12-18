"""
QUESTION:
Create a function `store_in_dict` that takes a dictionary as input where the values can be lists, dictionaries, or other types of data. Convert all the lists in the dictionary into tuples and keep the original nested structure intact. If a value is a dictionary, recursively call `store_in_dict` to handle nested dictionaries. The function should return the resulting dictionary with tuples.

The input dictionary can be created from a JSON string using `json.loads()` function. If the JSON string is invalid, the function `json.loads()` will raise a `JSONDecodeError` exception. 

The dictionary values can be of any type, but the function only needs to handle lists and dictionaries. If the dictionary contains other types of data, they should be left unchanged.
"""

def store_in_dict(data_dict):
    storage_dict = {}
    for key, value in data_dict.items():
        if type(value) == list:
            value = tuple(item for item in value)
        elif type(value) == dict:
            value = store_in_dict(value)
        storage_dict[key] = value
    return storage_dict